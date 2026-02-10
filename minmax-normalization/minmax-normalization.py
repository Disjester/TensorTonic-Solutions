import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    min_vals = np.min(X, axis=axis, keepdims=True)
    max_vals = np.max(X, axis=axis, keepdims=True)
    X_normalized = (X - min_vals) / (max_vals - min_vals + eps)
    
    return X_normalized