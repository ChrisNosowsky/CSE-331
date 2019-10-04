import math


class Graph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        # You may put any required initialization code here

    def insert_edge(self, u, v, w):
        pass

    def degree(self, v):
        return 0

    def are_connected(self, u, v):
        return False

    def is_path_valid(self, path):
        return False

    def edge_weight(self, u, v):
        return math.inf

    def path_weight(self, path):
        return math.inf

    def does_path_exist(self, u, v):
        return False

    def find_min_weight_path(self, u, v):
        return []

    def is_bipartite(self):
	    return False
