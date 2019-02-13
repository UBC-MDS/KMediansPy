# Feb 9, 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script is the package for KMediansPy

import numpy as np
import pandas as pd

# remove this one once we switch out the distance function
from scipy.spatial import distance




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


def summary(x, medians, labels):
    """
    Generates a table to display the cluster labels, the x and y coordinates of the cluster medians, 
    number of points in each cluster, the average distance within the cluster, 
    the maximum distance within the cluster and the minimum distance within the cluster. 
    
    
    Parameters
    ----------
    x: 2D array
       dataset, must only be 2D (x & y coordinates)
    
    medians: 2D array
       X and y coordinates of each cluster median
    
    labels:  1D array
        Array with the assignment of the cluster for each set of point in the dataset 
    
    Returns 
    -------
    summary dataframe
        Returns a dataframe with 7 columns and the number of rows will match the number of clusters. The labels of the columns: 
        Cluster labels, X Coordinates of Final Medians, Y Coordinates of Final Medians,  Number of Points in a Cluster, Average Distance within Cluster,
        Minimum Distance within Cluster, Maximum Distance within Cluster
    
    """
      # cluster labels for table
    cluster_labels = np.unique(labels)
    
    #x & y coordinates for table 
    xcoor_medians = []
    ycoor_medians = []
    for i in medians:
        xcoor_medians.append(i[0])
        ycoor_medians.append(i[1])
    
    # create dict to get label with index of position
    dict_label_index = {}
    for i in cluster_labels:
        dict_label_index[i] = [index for index, value in enumerate(labels) if value == i]
    
    # intilize empty lists
    number_points = []
    avg_distance = []
    max_distance = []
    min_distance = []
    for i in cluster_labels:
        # loop into the cluster to get number of points, max, min, and average (of a single cluster)
        new_list = []
        # loop to get the index values for the cluster
        for j in dict_label_index[i]:
            new_list.append(x[j])
        myarray = np.array(new_list) 
        med_dat =np.array([medians[i]])
    
    # need to switch out for our distance function
        dist_test = distance.cdist(myarray, med_dat, 'minkowski', p=1)
    
    # calculate average, max and min
        avg_distance.append(np.mean(dist_test))
        max_distance.append(np.max(dist_test))
        min_distance.append(np.min(dist_test))
    # count the number of points in each cluster
        number_points.append(len(dict_label_index[i]))
    
    # generate the dataframe to print to screen
    df_data = {"Cluster Label":cluster_labels, 
         "X Coordinates of Final Medians":xcoor_medians,
         "Y Coordinates of Final Medians":ycoor_medians,
         "Number of Points in a Cluster":number_points,
         "Average Distance within Cluster":avg_distance,
         "Maxiumum Distance within Cluster":max_distance,
         "Minimum Distance within Cluster":min_distance}
    output_df = pd.DataFrame(data=df_data)
    
    return output_df
