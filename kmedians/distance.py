
# coding: utf-8

# In[ ]:


def distance(X, medians):
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
    dist: 2D array
        Distance between each point and each median
    
    """
    k = medians.shape[0]
    n = X.shape[0]
    dist = np.zeros((n,k),dtype='int32')
    
    for k in range(k):
        for i in range(n):
            dist[i,k] = abs(X[i,0]-medians[k,0])+abs(X[i,1]-medians[k,1])
    return dist

