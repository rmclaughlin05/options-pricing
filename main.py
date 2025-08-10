from black_scholes import black_scholes
from monte_carlo import monte_carlo_pricing
from visuals import plot_price_distribution
import numpy as np

# Parameters
S0 = 100     # Stock price today
K = 105      # Strike price
T = 1        # Time to maturity (years)
r = 0.05     # Risk-free rate
sigma = 0.2  # Volatility
num_sims = 100000

# Black–Scholes
bs_price = black_scholes(S0, K, T, r, sigma, option_type='call')

# Monte Carlo
import numpy as np
Z = np.random.standard_normal(num_sims)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
mc_price = np.exp(-r * T) * np.mean(np.maximum(ST - K, 0))

# Plot distribution
plot_price_distribution(ST, K)

# Print results
print(f"Black–Scholes Price: {bs_price:.4f}")
print(f"Monte Carlo Price:   {mc_price:.4f}")
