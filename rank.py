# coding=utf8

from libs.ranking.nodes.node_ranking import NodeRanking
import networkx as nx
import sys
import os
import pickle

if __name__ == '__main__':
    datafn = sys.argv[1]
    method = sys.argv[2]  # degree, pagerank, percolation
    output = sys.argv[3]
    name = datafn.split('/')[-1].split('.')[0]

    print(method)

    try:
        G = nx.read_gpickle(datafn)
    except:
        try:
            with open(datafn, 'rb') as f:
                G = pickle.load(f, encoding='latin1')
        except Exception as ex:
            print(ex)
            print('Could not open graph: {}'.format(datafn))
            sys.exit(0)

    for n in G.nodes():
        G.node[n] = {}

    if method == 'percolation':
        G = max(nx.connected_component_subgraphs(G), key=len)

    print(nx.info(G))

    ns = NodeRanking.get_instance(method, G)

    flag = 0
    for s in ['asc', 'desc']:
        fn = os.path.join(output, '{}_{}_{}.pickle'.format(name, method, s))
        if os.path.exists(fn):
            flag += 1

    if flag < 2:
        ns.compute_node_scores()

        for s in ['asc', 'desc']:
            fn = os.path.join(output, '{}_{}_{}.pickle'.format(name, method, s))

            if os.path.exists(fn):
                print('{} {} already exists!'.format(method,s))
                continue

            # print(s)
            nodes = ns.rank_nodes(s)
            # print(nodes)

            with open(fn,'wb') as f:
                pickle.dump(nodes, f)

            print('{} saved!'.format(fn))
    else:
        print('nothing to do.')


