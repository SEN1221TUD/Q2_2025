
## Checklist

In the checklist below, you can find important topics and tasks that you should be familiar with before the practical exam. Make sure to practice these topics using the lab session as well as using the toy [datasets](toy_datasets). Importantanly, to simulate the exam environment use only the provided resources, meaning WITHOUT ChatGPT, CoPilot, etc.

#### Python basics
- [ ] I can work with basic Python data structures (e.g. lists and dictionaries)
- [ ] I can read and understand Python code snippets
- [ ] I am familiar with the packages used during the course: e.g. pandas, biogeme, matplotlib, seaborn, torch
- [ ] I can navigate and find information in the package/library documentation (e.g. pandas, biogeme) provided in the Documentation-hub (thus without internet or search options)

#### Working with Jupyter Notebooks
- [ ] I can open and navigate a Jupyter Notebook from a file
- [ ] I can import new libraries
- [ ] I can import methods and functions from libraries
- [ ] I can run and add new cells in the Jupyter Notebook
- [ ] I can handle errors in Jupyter Notebook
- [ ] I can restart the kernel in case the notebook crashes

#### Data exploration
- [ ] I can load dataset (e.g. CSV, dat, txt, etc.) into a pandas DataFrame
- [ ] I can calculate basic statistics (mean, median, mode, standard deviation, etc.) e.g. to see if the sample is representative.
- [ ] I can prepare the data for analysis (e.g. handle missing values, encode categorical variables)
- [ ] I can visualise the data using libraries such as Matplotlib or Seaborn using different types of plots (e.g. histograms, scatter plots, etc.)

#### Discrete choice modelling with Biogeme
- [ ] I can import methods from a custom Python module (i.e. a .py file containing reusable functions), in this case: `bio_estimation_fcns.py`
- [ ] I can create a biogeme database in Biogeme from a pandas DataFrame
- [ ] I can create define variables in Biogeme, using the Variable() method
- [ ] I can create define model parameters in Biogeme, using the Beta() method
- [ ] I can define utility functions, including linear and nonlinear specifications and with interaction terms
- [ ] I can reparameterise utility functions to WTP space
- [ ] I can define the availability conditions in Biogeme
- [ ] I can specify various types of discrete choice models using Biogeme, including MNL, Mixed Logit models that account for random taste variation and nesting structures
- [ ] I can estimate the various types of discrete models using the Biogeme
- [ ] I can parameterise Mixed Logit models with different distributions (e.g. normal, log-normal, uniform)
- [ ] I can print and interpret the output of a Biogeme model estimation
- [ ] I can compute (mean) WTP estimates from an estimated discrete model
- [ ] I can plot distributions of random parameters from a Mixed Logit model
- [ ] I can evaluate a choice model's performance using metrics, such as log-likelihood and rho-squared
- [ ] I can conduct a likelihood ratio test to compare two nested models
- [ ] I can apply an estimated model for forecasting choice probabilities on a new dataset

#### Data-driven and hybrid choice model with PyTorch
- [ ] I can prepare data for training a data-driven or hybrid choice model using PyTorch, including:
  - [ ] train/test split creation
  - [ ] data scaling
  - [ ] tensor creation
  - [ ] data loaders creation
- [ ] I can define a neural network architecture using PyTorch
- [ ] I can define a loss function and an optimiser in PyTorch
- [ ] I can define the hyperparameters for training a data-driven or hybrid choice model using PyTorch
- [ ] I can train a data-driven or hybrid choice model using PyTorch
- [ ] I can evaluate the performance of a data-driven or hybrid choice model using appropriate metrics
- [ ] I can define a neural network architecture using PyTorch
- [ ] I can define a loss function and an optimiser in PyTorch
- [ ] I can define the hyperparameters for training a data-driven or hybrid choice model using PyTorch
- [ ] I can train a data-driven or hybrid choice model using PyTorch, including:
  - [ ] forward pass
  - [ ] backward pass
  - [ ] weight updates
- [ ] I can evaluate the performance of a data-driven or hybrid choice model using appropriate metrics