
# coding: utf-8

# In[1]:


import numpy as np
import pytest


# In[2]:


X = np.array([[1, 2],[9, 8],[1.5, 2]])


# In[3]:


def test_toy_data_summary():

    """

    Tests that the algorithm correctly clusters toy example

    """
    X = np.array([[1, 2],[4, 5],[6, 2],[9, 8]])
    medians, labels = KMedians(X, 2)
    df = summary(medians, labels)
    
    assert np.equal(df.shape[0], 2)
    assert np.equal(df['Number of points in a cluster'].sum(), 3)
    assert np.equal(max(distance), 9)
    assert np.equal(min(distance), 1)
    assert np.equal(np.mean(distance), 6)


# In[4]:


def test_number_of_points_in_clusters(data, k):

    """

    Tests that the algorithm preserves the total number of data points 

    """
    medians, labels = KMedians(data, k)
    df = summary(medians, labels)
    
    assert np.equal(df['Number of points in a cluster'].sum(), data.shape[0])


# In[5]:


def test_number_of_clusters(data, k):

    """

    Tests that the algorithm correctly predicts the total number of clusters 

    """
    medians, labels = KMedians(data, k)
    df = summary(medians, labels)
    
    assert np.equal(np.unique(labels), k)

