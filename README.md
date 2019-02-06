
| **Team Members** |
| -- |
| (Sreya Guha)[https://github.com/sreyaguha] |
| (Ayla Perason)[https://github.com/aylapear] |
| (Fan Nei)[]  |
| (Pan Ting)[] |

# About

Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). In k-medians clustering, we partition `n` observations into `k` clusters. It calculates the median for each cluster to determine its centroid. The `kmedians` package performs k-medians clustering on the dataset entered by the users and returns ___________. This can prove to be an extremely beneficial package as k-medians is more robust to outliers than the arithmetic mean(k-means). The objective of this package is to provide a robust clustering method to solve some of the issues related to outliers and missing data.

# Functions included

The three main functions in the package are :

1. `distance` function

      - The function helps to calculate the Manhattan distance between each pair of the two collection inputs. This function takes as input 
      1. An `mxn` array of `m` original observations in an `n`-dimensional space
      2. An `pxk` array of `p` original observations in an `k`-dimensional space
      It returns a `mxp` distance matrix. For each `i` and `j`, the mteric `distance(u=X[i], v=Y[j])` is computed and stored in the `ij`th entry

2. `kmedian` function

      - A quick implementation of k-medians. It takes as input 
        1. A 2D array of data
        2. The desired number of clusters
      It returns 
        1. A 2D array of the medians
        2. 1D array of labels (the clusters the points belongs to)

3. `summary` function

      - This function generates the descriptive statistics that summarize the implementation of the `kmedians` function on the input data. It returns a           dataframe that contains information about the model run such as the number of clusters, the number of points in each cluster, the inter and intra           cluster distance


# Usage Scenario

k-median is more robust to noise and outliers as compared to k-means. Let's look at an example, suppose we want to cluster on one dimension with k=2. One cluster has most of its members around 1000 and the other around -1000; but there is an outlier (or noise) at 100000. It obviously belongs to the cluster around 1000 but k-means will put the center point away from 1000 and towards 100000. This may even make some of the members of the 1000 cluster (say a member with value 500) to be assigned to the -1000 cluster. k-median will select one of the members around 1000 as the median, it'll probably select one that is bigger than 1000, but it will not select an outlier.
Thus we would want to use 

# Existing packages in the Python environment

`pyclustering` : pyclustering is a Python, C++ data mining library (clustering algorithm, oscillatory networks, neural networks). The library provides Python and C++ implementations (via CCORE library) of each algorithm or model (e.g. K-Means, K-Means++, K-Medians, etc.) 

# Subject to change

The above ideas are presented as a part of the initial proposal. However, they could be subject to change in the following milestones based on the project timeline or technical complexity.

