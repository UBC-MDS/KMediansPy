# Feb 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script is the summary function in the


import numpy as np
import pandas as pd
from KMediansPy.distance import distance



def summary(x:np.ndarray, medians:np.ndarray, labels:np.ndarray) -> pd.DataFrame:
    """
    Generates a table to display the cluster labels, the x and y coordinates of the cluster medians,
    number of points in each cluster, the average distance within the cluster,
    the maximum distance within the cluster and the minimum distance within the cluster.


    Parameters
    ----------
    x: 2D array of order mx2
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
        # calculate distance between median and points in cluster
        dist_test = distance(myarray, med_dat)

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
