import knapsack_solvers as ks
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
        print(i)
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
greedy = [60.0, 492.2, 867.8, 1010.8, 1203.6, 1118.8, 1362.6, 1464.8, 1632.0, 1717.8]
random1 = [60.0, 497.2, 876.4, 1038.6, 1219.6, 1123.4, 1382.0, 1504.6, 1637.2, 1722.4]
fee = [60.0, 497.2, 876.4, 1038.6, 1219.6, 1123.8, 1382.0, 1500.0, 1637.2, 1722.4]
size = [60.0, 497.2, 876.4, 1038.6, 1219.6, 1123.8, 1382.0, 1504.6, 1637.2, 1722.4]
relation = [60.0, 497.2, 876.4, 1038.6, 1219.6, 1123.8, 1382.0, 1504.6, 1637.2, 1722.4]
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
plot()
