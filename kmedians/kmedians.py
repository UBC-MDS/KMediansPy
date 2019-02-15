# Feb 14, 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script is the package for KMediansPy


# import numpy as np
# import random as random


def KMedians(x, n_cluster):
    """
    Groups the points in your dataset ,X, into the desired number of clusters, based on the median distance between the points. 
    This function uses random intilization to assign the first medians and then will update the medians and 
    the group assignments until the assignment does not change. 
    
    Parameters
    ----------
    x: 2D array of order mx2
       The dataset being clustered
    
    n_cluster: integer
      The desired number of clusters 
    
    Returns
    -------
    medians: 2D array
        The coordinates of the medians for each cluster
    
    labels: 1D array
        Array that has the assignment of the cluster for each point in the dataset 
        
    """
    
    n = x.shape[0]
    u = np.zeros((n_cluster,n),dtype='int32')
    # assign random centers to the clusters
    medians = x[np.random.choice(range(0, n), size=n_cluster, replace=False)]
    
    m = medians.shape[0]
    l = medians.shape[1]
    
    # while the medians do not change, run the loop
    prev_medians =np.zeros((m,l),dtype='int32')
    while (medians!= prev_medians).any():
        for i in range(0, n_cluster):
            dist = distance(x, medians, 'minkowski', p=1)
            labels = np.argmin(dist, axis=1)
            u[labels, range(0,n)] = 1
            # assign new medians
            medians[i] = np.median(x[u[i]==1],axis=0)
        prev_medians = medians
            
    return (medians, labels)

