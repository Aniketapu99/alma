import numpy as np
import pandas as pd

def alma(series, window=9, offset=0.85, sigma=6):
    m = offset * (window - 1)
    s = window / sigma
    weights = [np.exp(-(i - m) ** 2 / (2 * s ** 2)) for i in range(window)]
    weights = np.array(weights) / sum(weights)
    return pd.Series(series).rolling(window).apply(lambda x: np.dot(x, weights), raw=True)
