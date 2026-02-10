import numpy as np

def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    values = np.array(values)
    
    expanded_vals = np.broadcast_to(values[:, np.newaxis], (values.shape[0], degree + 1))
    
    col_indices = np.arange(expanded_vals.shape[1])
    
    result = np.power(expanded_vals, col_indices)
    
    return result.tolist()