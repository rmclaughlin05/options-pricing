import numpy as np
import matplotlib.pyplot as plt

def plot_price_distribution(ST, K): 
    plt.hist(ST, bins=50, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(K, color='red', linestyle='dashed', linewidth=2)
    plt.title('Simulated Stock Price Distribution at Maturity')
    plt.xlabel('Stock Price')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()