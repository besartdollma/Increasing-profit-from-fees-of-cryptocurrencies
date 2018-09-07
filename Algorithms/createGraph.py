import createMemoryPool
import networkx as nx


# It creates a graph of the memory pool at time with the given sample number

def create_graph(time, sample_number):
    mem_pool = createMemoryPool.createMemoryPool(time, sample_number)
    # mem_pool is a list that contains elements of the type:
    # (id,[ancestors_id],fee,size)
    G = nx.DiGraph()
    for transaction in mem_pool:
        G.add_node(transaction[0], fee=transaction[2], size=transaction[3])

    for transaction in mem_pool:
        for parent in transaction[1]:
            if parent not in G.nodes():
               print(parent)
            G.add_edge(parent, transaction[0])
    return G


