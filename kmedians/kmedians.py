# Feb 9, 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script is the package for KMediansPy



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
    return dist


def kmedians(X, num_clusters):
    """
    Groups the points in your dataset ,X, into the desired number of clusters, based on the median distance between the points. 
    This function uses random intilization to assign the first medians and then will update the medians and 
    the group assignments until the assignment does not change. 
    
    Parameters
    ----------
    X: 2D array
       The dataset being clustered
    
    num_clusters: integer
      The desired number of clusters 
    
    Returns
    -------
    medians: 2D array
        The coordinates of the medians for each cluster
    
    labels: 1D array
        Array that has the assignment of the cluster for each point in the dataset 
    """
    return medians, labels


def summary(X, medians, labels):
    """
    Generates a table to display the cluster labels, the coordinates of the cluster medians, 
    number of points in each cluster, the average distance within the cluster, 
    the maximum distance within the cluster and the minimum distance within the cluster. 
    
    
    Parameters
    ----------
    X: 2D array
       The dataset being clustered
    
    medians: 2D array
       Coordinates of each cluster median
    
    labels:  1D array
        Array with the assignment of the cluster for each point in the dataset 
    
    Returns 
    -------
    dataframe
        Returns a dataframe with 6 columns and number of rows will be the number of clusters. The labels of the columns: 
        Cluster labels, Median Coordinates, Number of Points in Cluster, Average Distance, Minimum Distance, Maximum Distance
    
    """
    return dataframe
