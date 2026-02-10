import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    rater1_np = np.array(rater1)
    rater2_np = np.array(rater2)
    n = rater1_np.shape[0]

    p_0 = np.sum(rater1_np == rater2_np) / n

    labels_1, counts_1 = np.unique(rater1_np, return_counts = True)
    labels_2, counts_2 = np.unique(rater2_np, return_counts = True)

    labels_1_dict = dict(zip(labels_1, counts_1))
    labels_2_dict = dict(zip(labels_2, counts_2))
    
    labels = set(labels_1).union(set(labels_2))

    p_e = 0

    for label in labels:
        p_e += (labels_1_dict.get(label, 0))/n * (labels_2_dict.get(label, 0))/n

    if p_e == 1:
        return 1

    k = (p_0-p_e)/(1-p_e)
    
    return k