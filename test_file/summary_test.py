
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
    Tests that the algorithm correctly clusters toy example
    """
    np.random.seed(1)
    X = np.array([[1, 2],[4, 5],[6, 2],[9, 8]])
    medians, labels = KMedians(X, 2)
    df = summary(X, medians, labels)

    assert np.equal(df.shape[0], 2)
    assert np.equal(df['Number of Points in a Cluster'].sum(), 4)
    assert np.equal(df['Maxiumum Distance within Cluster'].sum(), 3.0)
    assert np.equal(df['Minimum Distance within Cluster'].sum(), 2.0)
    assert np.equal(round(df['Average Distance within Cluster'].sum(), 2), 2.67)


def test_number_of_points_in_clusters():
    """
    Tests that the algorithm preserves the total number of data points
    """

    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)

    assert np.equal(df['Number of Points in a Cluster'].sum(), data.shape[0])



def test_number_of_clusters():
    """
    Tests that the algorithm correctly predicts the total number of clusters
    """

    medians, labels = KMedians(data, k)
    df = summary(data, medians, labels)

    assert np.equal(len(df['Cluster Label']), k)
    