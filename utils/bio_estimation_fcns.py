import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import log, exp, Variable, MonteCarlo, exp, bioMultSum
import matplotlib.pyplot as plt
import numpy as np


# This function estimates the MNL model and returns the estimation results
# input values: utilities for all three alternatives, the choices, the database, and the model name

def estimate_mnl(V, AV, CHOICE, database, model_name):

    # Define the choice model: The function models.logit() computes the MNL choice probabilities of the chosen alternative given the V. 
    prob = models.logit(V, AV, CHOICE)

    # Define the log-likelihood by taking the log of the choice probabilities of the chosen alternative
    LL = log(prob)
   
    # Create the Biogeme object containing the object database and the formula for the contribution to the log-likelihood of each row using the following syntax:
    biogeme = bio.BIOGEME(database, LL)
    
    # The following syntax passes the name of the model:
    biogeme.modelName = model_name

    # Some object settings regaridng whether to save the results and outputs 
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False

    # Syntax to calculate the null log-likelihood. The null-log-likelihood is used to compute the rho-square 
    biogeme.calculate_null_loglikelihood(AV)

    # This line starts the estimation and returns the results object.
    results = biogeme.estimate()
    return results

def simulate_mnl(V, AV, CHOICE, database, betas, model_name):

    # # Simulate the model on the test database

    # Compute the denominator: sum of exp(V[i]) for all available alternatives
    denominator = sum(exp(V[i]) * AV[i] for i in V)

    # Compute the choice probabilities for each alternative
    simulate = {}
    for i in V:
        simulate[f'P{i}'] = (exp(V[i]) / denominator) * AV[i]
        simulate[f'V{i}'] = V[i]

    # Compute the probability of the chosen alternative
    simulate['Pchosen'] = sum((CHOICE == i) * (exp(V[i]) / denominator) for i in V)

    # Run the simulation
    biogeme_sim = bio.BIOGEME(database, simulate)
    Psim = biogeme_sim.simulate(betas)

    # Compute the log-likelihood of the simulated data
    LLsim = np.log(Psim['Pchosen']).sum()

    LLnull = biogeme_sim.calculate_null_loglikelihood(AV)

    rho_square = 1 - (LLsim / LLnull)

    # Add the results to a dictionary
    simresults ={"V1": Psim['V1'], "V2": Psim['V2'],"P1": Psim['P1'], "P2": Psim['P2'],"Pchosen": Psim['Pchosen'], "LL": LLsim, "rho_square": rho_square,"model_name": model_name}
    
    return simresults

# This function estimates the cross-sectional MXL model and returns the estimation results
def estimate_mxl(V,AV,CHOICE,biodata,model_name, num_draws = 100):
    
    # The conditional probability of the chosen alternative is a logit
    condProb = models.logit(V, AV ,CHOICE)

    # The unconditional probability is obtained by simulation
    uncondProb = MonteCarlo(condProb)

    # The Log-likelihood is the log of the unconditional probability
    LL = log(uncondProb)

    # Create the Biogeme estimation object containing the data and the model
    biogeme = bio.BIOGEME(biodata , LL, number_of_draws=num_draws)

    # Set reporting levels
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False
    biogeme.modelName = model_name

    # Estimate the parameters and print the results
    results = biogeme.estimate()
    return results

# This function estimates the panel MXL model and returns the estimation results
def estimate_panel_mxl(V,AV,CHOICE,obs_per_ind,biodata_wide,model_name, num_draws = 100):

    # The conditional probability of the chosen alternative is a logit
    condProb = [models.loglogit(V[q], AV, CHOICE[q]) for q in range(obs_per_ind)] 

    # Take the product of the conditional probabilities
    condprobIndiv = exp(bioMultSum(condProb))   # exp to convert from logP to P again

    # The unconditional probability is obtained by simulation
    uncondProb = MonteCarlo(condprobIndiv)

    # The Log-likelihood is the log of the unconditional probability
    LL = log(uncondProb)

    # Create the Biogeme estimation object containing the data and the model
    num_draws = num_draws
    biogeme = bio.BIOGEME(biodata_wide , LL, number_of_draws=num_draws)

    # Compute the null loglikelihood for reporting
    # Note that we need to compute it manually, as biogeme does not do this for panel data
    biogeme.nullLogLike = biodata_wide.get_sample_size() * obs_per_ind * np.log(1 / len(V[0]))

    # Set reporting levels
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False
    biogeme.modelName = model_name    

    # Estimate the parameters and print the results
    results = biogeme.estimate()
    return results

def print_results(results):
    
    # Print the estimation statistics
    print(f'\n')
    if len(results.short_summary().strip().split('\n')) <=8:
        print(results.print_general_statistics())
    else:
        print(results.short_summary())

    # Get the model parameters in a pandas table and  print it
    beta_hat = results.get_estimated_parameters()
    
    # Round the results to suitable decimal places
    beta_hat = beta_hat.round(4)
    beta_hat['Rob. t-test']  = beta_hat['Rob. t-test'].round(2)
    beta_hat['Rob. p-value'] = beta_hat['Rob. p-value'].round(2)
    print(beta_hat)

def get_beta_param(params, name):
    """Get parameter value ignoring case and allowing B_, b_, or beta_ as prefixes."""
    name = name.lower()
    for key in params:
        if key.lower() == name or (key.endswith(name) and key.startswith(('B_','b_', 'beta_', 'mu_'))):
            return float(params[key])
    raise KeyError(f"Parameter for '{name}' not found.")

def get_sigma_param(params, name):
    """Get parameter value ignoring case and allowing sigma_, S_, or sigma_ as prefixes."""
    name = name.lower()
    for key in params:
        if key.lower().endswith(name) and key.lower().startswith(('sigma_', 'S_')):
            return float(params[key])
    raise KeyError(f"Parameter for '{name}' not found.")

def plot_distributions(results, distr_types, xmin, xmax, xlabel=None):

    parts = list(distr_types)
    fig, ax = plt.subplots(
        1, len(parts),
        figsize=(6 * len(parts), 5),
        sharey=False
    )
    if len(parts) == 1:
        ax = [ax]

    x = np.linspace(xmin, xmax, 500)
    if any(v['dist'] == 'lognormal' for v in distr_types.values()):
        x = x[x != 0]  # lognormal is not defined at 0

    params = results.get_beta_values()
    
    for i, part in enumerate(parts):
        mu = get_beta_param(params, f'{part}')
        sigma = abs(get_sigma_param(params, f'{part}'))

        spec   = distr_types[part]
        d_type = spec['dist']
        sign   = spec.get('sign', 1)              # default +1

        # ------------------------------------------------------------------
        # pick the pdf and mean formula for the requested distribution
        # ------------------------------------------------------------------
        if d_type == 'normal':
            mean = mu
            pdf  = (1 / (sigma * np.sqrt(2*np.pi))
                   ) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

        elif d_type == 'lognormal':
            raw_mean = np.exp(mu + 0.5 * sigma ** 2)   # > 0 by definition
            mean     = sign * raw_mean

            # Base pdf lives on the positive real line
            x_pos    = np.abs(x)
            base_pdf = (1 / (x_pos * sigma * np.sqrt(2*np.pi))
                       ) * np.exp(-((np.log(x_pos) - mu) ** 2) / (2 * sigma ** 2))

            # Flip to the requested side of the axis
            if sign < 0:
                pdf = np.where(x < 0, base_pdf, 0)
            else:
                pdf = np.where(x > 0, base_pdf, 0)

        else:
            raise ValueError(f"Unknown distribution type: {d_type}")

        # ------------------------------------------------------------------
        # draw
        # ------------------------------------------------------------------
        ax[i].plot(x, pdf, label=d_type)
        ax[i].axvline(0, ls='--', c='k')
        ax[i].axhline(0, ls='-', c='k')

        ax[i].set_title(f'{part}: {d_type}\nmean = {mean:.3g}')
        if xlabel is not None:
            ax[i].set_xlabel(xlabel)
        else:
            ax[i].set_xlabel('Marginal utility')
        if i == 0:
            ax[i].set_ylabel('PDF')
        ax[i].legend()

    plt.tight_layout()
    plt.show()