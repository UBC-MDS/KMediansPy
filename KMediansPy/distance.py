# Feb 9, 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script is the package for KMediansPy

import numpy as np

def distance(x, medians):
    """
    Calculates the Manhanttan distance between the medians and every point in the dataset

    Parameters
    ----------
    x: 2D array
       The dataset being clustered

    medians: 2D array
       Medians of the clusters

    Returns
    -------
    distance: 2D array
        Distance between each point and each median

    """

    if not isinstance(x, np.ndarray):
        raise TypeError("Dataset is not an array")

    if not isinstance(medians, np.ndarray):
        raise TypeError("Median values entered is not an array")

     if x.shape[0] == 0:
        raise IndexError("Dataset is empty")

    if x.shape[1] > 2:
       raise IndexError("Dataset should be of order mx2")

    if x.ndim == 1:
        raise IndexError("Data needs second dimension")

     if medians.shape[0] == 0:
        raise IndexError("No median values entered")

    k = medians.shape[0] #number of rows in the medians array
    n = x.shape[0] #number of columns in the dataset
    distance = np.zeros((n,k),dtype='int32')

    for k in range(k):
        for i in range(n):
            # calculating Manhattan distance between two sets of points
            distance[i,k] = abs(x[i,0]-medians[k,0])+abs(x[i,1]-medians[k,1])
    return distance
