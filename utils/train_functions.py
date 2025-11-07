import torch
import numpy as np
import matplotlib.pyplot as plt


def evaluate(model, criterion, data_loader):
    model.eval()  # Set the model to evaluation mode
    total_loss = 0.0

    with torch.no_grad():
        for inputs, labels in data_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            total_loss += loss.item()

    return total_loss

def evaluate_lmnl(model, criterion, data_loader):
    model.eval()  # Set the model to evaluation mode
    total_loss = 0.0

    with torch.no_grad():
        for x_mnl, x_mlp, labels in data_loader:
            outputs = model(x_mnl,x_mlp)
            loss = criterion(outputs, labels)
            total_loss += loss.item()

    return total_loss


def show_loss_plot(train_losses, test_losses, num_obs_train, num_obs_test, epoch_best=None):
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(np.array(train_losses)/num_obs_train, label='Training Loss')
    ax.plot(np.array(test_losses)/num_obs_test,   label='Test Loss')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Mean Loss per observation')
    ax.set_title(f'Training and Test Loss over Epochs\nLL_test: {-min(test_losses):0.2f}')
    
    if epoch_best is not None:
        ax.axvline(x=epoch_best, color='r', linestyle='--', label='Best Epoch')
    
    ax.legend(loc ='upper right')
    plt.show()

def print_model_summary(model):
    total_params = 0
    print(f"=== Model Summary ===")
    for name, param in model.named_parameters():
        if param.requires_grad:
            num_params = param.numel()
            total_params += num_params
            print(f"Layer: {name:20}|\t Weights: {num_params}")

    print(f"\nTotal trainable Weights: {total_params}")

    print("\n=== Layers ===")
    for layer in model.children():
        print(layer)