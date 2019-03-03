
# coding: utf-8

# In[1]:


import numpy as np
import pytest
from KMediansPy.summary import summary
from KMediansPy.KMedians import KMedians


data = np.array([[1, 2],[4, 5],[6, 2],[9, 8]])
k = 2


def test_toy_data_summary():
    """
    Tests that the algorithm correctly clusters toy example and tablulates data correctly
    """
    np.random.seed(1)
    X = np.array([[1, 2],[4, 5],[6, 2],[9, 8]])
    medians, labels = KMedians(X, 2)
    df = summary(X, medians, labels)

    assert np.equal(df.shape[0], 2)
    assert np.equal(df['Cluster Label'].sum(), 1), "Cluster Label doesn't match"
    assert np.equal(df['X Coordinates of Final Medians'].sum(), 13), "X Coordinate doesn't match"
    assert np.equal(df['Y Coordinates of Final Medians'].sum(), 10), "Y Coordinate doesn't match"
    assert np.equal(df['Number of Points in a Cluster'].sum(), 4), "Number of Points in a Cluster doesn't match"
    assert np.equal(round(df['Average Distance within Cluster'].sum(), 2), 2.67), "Average Distance within Cluster doesn't match"
    assert np.equal(df['Maxiumum Distance within Cluster'].sum(), 3.0), "Maxiumum Distance within Cluster doesn't match"
    assert np.equal(df['Minimum Distance within Cluster'].sum(), 2.0), "Minimum Distance within Cluster doesn't match" 

    
def test_number_of_points_in_clusters():
    """
    Tests that the algorithm preserves the total number of data points
    """

    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)

    assert np.equal(df['Number of Points in a Cluster'].sum(), data.shape[0]), 'Number of points in table does not match dataset'



def test_number_of_clusters():
    """
    Tests that the algorithm correctly predicts the total number of clusters
    """

    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)

    assert np.equal(len(df['Cluster Label']), k), 'Number of clusters does not match input k'

    
    
def correct_input_type():
    """
    Tests the input types for summary are numpy arrays
    """
    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)
    
    assert isinstance(data, np.ndarray), 'Data is not a numpy array'
    assert isinstance(labels, np.ndarray), 'Labels is not a numpy array'
    assert isinstance(medians, np.ndarray), 'Medians is not a numpy array'

    
    
def correct_output_type():
    """
    Tests that summary outputs a dataframe
    """
    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)

    assert isinstance(df, pd.DataFrame), 'Output is not a dataframe'
    