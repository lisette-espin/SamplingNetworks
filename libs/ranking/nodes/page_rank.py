from libs.ranking.nodes.node_ranking import NodeRanking
import networkx as nx

class PageRank(NodeRanking):

    def __init__(self, G):
        super(PageRank, self).__init__(G)

    def compute_node_scores(self):
        self.scores = [(pr,n) for n,pr in nx.pagerank(self.G).items()]
