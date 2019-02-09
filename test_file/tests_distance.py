import pytest
import numpy as np


def test_distance_calc():
    """
    Confirm that the correct distance is being calculated for each point from the medians by using a 
    simple toy dataset where the distances were calculated manually
    """
    
    X = np.array([[1, 2],[5, 4]])
    medians = np.array([[1, 2],[5, 4]])

    dist = distance(X, medians)
    
    assert dist == np.array([[6, 0], [0, 6]])
    
    
def test_dist_each_point(X, medians):
    """
    Confirm that the distance is being calculated for each point
    """

    dist = distance(X, medians)
    
    assert X.shape[0] == dist.shape[0]
    
    
    
def test_dist_each_cluster(X, medians):
    """
    Confirm that the distance is being calculated for each median
    """
    
    dist = distance(X, medians)
    
    assert medians.shape[0] == dist.shape[1]
    
    
    
def test_correct_input_type():
    """
    Confirm the input and outputs are numpy arrays and are all 2D arrays
    """
    
    dist = distance(X, medians)
    
    # check the type of the input/outputs are numpy arrays
    assert type(X) == np.ndarray
    assert type(medians) == np.ndarry
    assert type(dist) == np.ndarry
    
    # check that the input/outputs are 2D
    assert X.ndim == 2
    assert medians.ndim == 2
    assert dist.ndim == 2
      
    
    
    
    
    
    
    