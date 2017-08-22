from libs.ranking.nodes.node_ranking import NodeRanking
import networkx as nx

class Degree(NodeRanking):

    def __init__(self, G):
        super(Degree, self).__init__(G)

    def compute_node_scores(self):
        self.scores = [(self.G.degree(n),n) for n in self.G.nodes()]

