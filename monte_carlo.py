import numpy as np 

def monte_carlo_pricing(S0, K, T, r, sigma, option_type='call', num_simulations=10000):
    """Price Euro Options using Monte Carlo simulation."""
    # Simulate end-of-period stock prices
    Z = np.random.standard_normal(num_simulations)
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

    # Calculate payoffs
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Discount payoffs back to present value
    price = np.exp(-r * T) * np.mean(payoffs)
    
    return price