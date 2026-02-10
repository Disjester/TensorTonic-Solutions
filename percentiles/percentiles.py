import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.array(x)
    q = np.array(q)

    n = x.shape[0]

    sorted_x = np.sort(x)

    indices = (n - 1) * q / 100
    
    low_indices = np.floor(indices).astype(int)
    high_indices = np.ceil(indices).astype(int)
    diff, _ = np.modf(indices)
    
    percentiles = sorted_x[low_indices] + (sorted_x[high_indices] - sorted_x[low_indices]) * diff

    return percentiles