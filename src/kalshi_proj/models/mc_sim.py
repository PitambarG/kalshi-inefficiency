
import numpy as np

def gbm_paths(s0: float, mu: float, sigma: float, T: float, steps: int, n_paths: int, rng=None):
    rng = rng or np.random.default_rng(42)
    dt = T / steps
    paths = np.empty((n_paths, steps+1))
    paths[:,0] = s0
    for t in range(1, steps+1):
        z = rng.standard_normal(n_paths)
        paths[:,t] = paths[:,t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    return paths

def prob_threshold(paths: np.ndarray, thresh: float) -> float:
    return (paths[:,-1] > thresh).mean()
