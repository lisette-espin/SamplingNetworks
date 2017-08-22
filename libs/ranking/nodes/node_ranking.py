from heapq import *

class NodeRanking(object):

    def __init__(self, G):
        self.G = G
        self.scores = None

    def compute_node_scores(self):
        return

    def rank_nodes(self, order):
        heapify(self.scores)
        if order == 'asc':
            return [n for s, n in nsmallest(len(self.scores), self.scores)]
        return  [n for s,n in nlargest(len(self.scores),self.scores)]

    @staticmethod
    def get_instance(method, G):
        from libs.ranking.nodes.degree import Degree
        from libs.ranking.nodes.optimal_percolation import OptimalPercolation
        from libs.ranking.nodes.page_rank import PageRank

        if method == 'degree':
            return Degree(G)

        elif method == 'percolation':
            return OptimalPercolation(G)

        elif method == 'pagerank':
            return PageRank(G)