import knapsack solvers as ks
import networkx as nx
import random
import matplotlib.pyplot as plt

AVERAGE_RUN = 5
BLOCK_SIZE = 1000
#######################################################################################
def create_random_graph(num_of_nodes, with_edges):
    G = nx.DiGraph()
    for i in range(num_of_nodes):
        G.add_node(i,size=random.randint(1,200),fee=random.randint(1,100))
    if with_edges:
        for i in range(num_of_nodes):
            G.add_edge(random.randint(0,num_of_nodes-1),random.randint(0,num_of_nodes-1))
    return G
#######################################################################################
def create_data():

    nodes = []
    fee = []
    random = []
    relation = []
    size = []
    greedy = []

    for i in range(1,100,10):

        nodes.append(i)
        fee_sum = 0
        random_sum = 0
        relation_sum = 0
        size_sum = 0
        greedy_sum = 0

        for j in range(AVERAGE_RUN):
            G = create_random_graph(i, False)
            greedy_sum += ks.greedy(G, BLOCK_SIZE)
            fee_sum += ks.greedy_epsilon(G, 0.05, BLOCK_SIZE, 'fee')
            random_sum += ks.greedy_epsilon(G, 0.05, BLOCK_SIZE, 'random')
            relation_sum += ks.greedy_epsilon(G, 0.05, BLOCK_SIZE, 'relation')
            size_sum += ks.greedy_epsilon(G, 0.05, BLOCK_SIZE, 'size')

        greedy.append(greedy_sum/AVERAGE_RUN)
        fee.append(fee_sum/AVERAGE_RUN)
        size.append(size_sum/AVERAGE_RUN)
        random.append(random_sum/AVERAGE_RUN)
        relation.append(relation_sum/AVERAGE_RUN)

    print("nodes = " + str(nodes))
    print("greedy = " + str(greedy))
    print("random = " + str(random))
    print("fee = " + str(fee))
    print("size = " + str(size))
    print("relation = " + str(relation))

#######################################################################################
#DATA CREATED FROM PREVIOUS FUNCTION FIGURE 9
nodes = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
greedy = [52.4, 577.6, 736.4, 976.0, 1127.0, 1360.2, 1490.8, 1488.8, 1590.4, 1824.0]
random1 = [52.4, 584.4, 743.0, 935.8, 1107.2, 1343.4, 1474.2, 1500.0, 1607.2, 1837.0]
fee = [52.4, 584.4, 747.8, 978.2, 1138.2, 1377.8, 1508.4, 1500.0, 1611.6, 1840.2]
size = [52.4, 584.4, 744.6, 965.4, 1127.6, 1307.8, 1422.4, 1498.6, 1614.6, 1840.0]
relation = [52.4, 584.4, 743.0, 914.4, 1087.4, 1361.4, 1474.8, 1497.8, 1605.8, 1828.2]
#######################################################################################
def relative(sol, opt):
    rel = []
    for i in range(len(sol)):
        rel.append((sol[i]-opt[i]))
    print(rel)
    return rel
#######################################################################################
def plot():
    plt.plot(nodes, relative(greedy,greedy), 'cv', label = 'Greedy')
    plt.plot(nodes, relative(random1,greedy), 'bo', label= 'Random')
    plt.plot(nodes, relative(fee, greedy),  'r*', label = 'Fee', markersize = '5')
    plt.plot(nodes, relative(size, greedy), 'gx', label = 'Size', markersize = '7')
    plt.plot(nodes, relative(relation, greedy), 'k+', label = 'Relation', markersize ='10')
    plt.xlabel("Number of Transactions")
    plt.ylabel("Profit relative to the greedy approximation")
    plt.legend(loc='center right')
    plt.show()
#######################################################################################