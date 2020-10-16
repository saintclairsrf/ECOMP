# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:35:17 2020

@author: saint
"""
import numpy as np
import igraph
import pandas as pd

# get the row, col indices of the non-zero elements in your adjacency matrix
conn_indices = np.where(a_numpy)

import igraph

# get the row, col indices of the non-zero elements in your adjacency matrix
conn_indices = np.where(a_numpy)

# get the weights corresponding to these indices
weights = a_numpy[conn_indices]

# a sequence of (i, j) tuples, each corresponding to an edge from i -> j
edges = zip(*conn_indices)

# initialize the graph from the edge sequence
G = igraph.Graph(edges=edges, directed=True)

# assign node names and weights to be attributes of the vertices and edges
# respectively
G.vs['label'] = node_names
G.es['weight'] = weights

# I will also assign the weights to the 'width' attribute of the edges. this
# means that igraph.plot will set the line thicknesses according to the edge
# weights
G.es['width'] = weights

# plot the graph, just for fun
igraph.plot(G, layout="rt", labels=True, margin=80)