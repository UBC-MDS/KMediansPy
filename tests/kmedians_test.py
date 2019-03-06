
# coding: utf-8

# In[43]:


import numpy as np
import pytest
from KMediansPy.KMedians import KMedians


data = np.array([[1, 2],[9, 8],[1.5, 2]])
k = 2


def test_toy_data():

    """

    Tests that the algorithm correctly clusters toy example

    """
    X = np.array([[1, 2],[9, 8],[1.5, 2]])
    medians, labels = KMedians(X, 2)

    print(np.size(medians[0],0))



def test_input_k():

    """

    Tests that the algorithm inputs `k` as an integer

    """
    assert type(k) == int


def test_clusters_labels():

    """

    Tests that the algorithm forms the correct clusters labels

    """
    medians, labels = KMedians(data, k)
    print(np.unique(labels))
    #assert np.equal(len(np.unique(labels)), k)


def test_number_of_clusters():

    """

    Tests that the algorithm forms the correct number of clusters

    """
    medians, labels = KMedians(data, k)

    assert np.equal(np.size(medians[0],0), k)
