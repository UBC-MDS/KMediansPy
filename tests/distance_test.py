# Feb 9, 2019
# Sreya Guha, Ayla Pearson, Fan Nie, Ting Pan
#
# This script tests the distance function for kmedians.py



import pytest
import numpy as np
from KMediansPy.distance import distance


## Helper Functions

def toy_data():
    """
    Generates simple data set and parameters to test
    """
    X = np.array([[1, 2],[5, 4]])
    medians = np.array([[1, 2],[5, 4]])
    dist = distance(X, medians)
    return X, medians, dist



## Test Functions

def test_distance_calc():
    """
    Confirm that the correct distance is being calculated for each point from the medians by using a
    simple toy dataset where the distances were calculated manually
    """
    _, _, dist = toy_data()
    assert np.all(dist) == np.all(np.array([[6, 0], [0, 6]]))



def test_dist_each_point():
    """
    Confirm that the distance is being calculated for each point
    """
    X, _, dist = toy_data()
    assert X.shape[0] == dist.shape[0]



def test_dist_each_cluster():
    """
    Confirm that the distance is being calculated for each median
    """
    _, medians, dist = toy_data()
    assert medians.shape[0] == dist.shape[1]



def test_correct_input_type():
    """
    Confirm the input and outputs are numpy arrays and are all 2D arrays
    """
    X, medians, dist = toy_data()
    # check the type of the input/outputs are numpy arrays
    assert type(X) == np.ndarray
    assert type(medians) == np.ndarray
    assert type(dist) == np.ndarray
    # check that the input/outputs are 2D
    assert X.ndim == 2
    assert medians.ndim == 2
    assert dist.ndim == 2


#%%

test_dist_each_point()
test_dist_each_cluster()
test_correct_input_type()
