import knapsack solvers as ks
import networkx as nx
import random
import time
import dependency knapsack solvers as dks
import matplotlib.pyplot as plt

AVERAGE_RUN = 10
BLOCK_SIZE = 10000
#######################################################################################
def create_random_graph(num_of_nodes, with_edges):
    G = nx.DiGraph()
    for i in range(num_of_nodes):
        G.add_node(i,size=random.randint(1,100),fee=random.randint(1,100))
    if with_edges:
        number_of_edges = random.randint(1,num_of_nodes**2)
        for i in range(number_of_edges):
            first = random.randint(0,num_of_nodes-1)
            second = random.randint(0,num_of_nodes-1)
            anc = nx.ancestors(G, first)
            if second in anc:
                continue
            G.add_edge(first, second)

    return G
#######################################################################################
def create_data():
    nodes = []
    greedy_without = []
    greedy_with = []

    for i in range(1, 150, 10):

        nodes.append(i)
        greedy_without_sum = 0
        greedy_with_sum = 0

        for j in range(AVERAGE_RUN):
            G1 = create_random_graph(i, False)
            start = time.time()
            ks.greedy(G1, BLOCK_SIZE)
            end = time.time()
            greedy_without_sum += end - start
            G2 = create_random_graph(i, True)
            start = time.time()
            dks.get_fee_greedy(G2, BLOCK_SIZE)
            end = time.time()
            greedy_with_sum += end - start

        greedy_without.append(greedy_without_sum/AVERAGE_RUN)
        greedy_with.append(greedy_with_sum/AVERAGE_RUN)

    print("nodes = " + str(nodes))
    print("greedy_without = " + str(greedy_without))
    print("greedy_with = " + str(greedy_with))

#######################################################################################
# DATA CREATED FROM THE PREVIOUS FUNCTION - FIGURE 12
nodes = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141]
greedy_without = [9.987354278564453e-05, 0.00010013580322265625, 9.999275207519531e-05, 0.0, 9.9945068359375e-05, 0.00020000934600830078, 9.992122650146485e-05, 0.0, 0.00019998550415039061, 0.0002999305725097656, 9.992122650146485e-05, 0.0, 0.00019998550415039061, 0.00019991397857666016, 9.9945068359375e-05]
greedy_with = [0.0, 0.0007995843887329101, 0.001299142837524414, 0.0035982131958007812, 0.004996800422668457, 0.007395434379577637, 0.009394097328186034, 0.013092279434204102, 0.016989374160766603, 0.020986413955688475, 0.02488439083099365, 0.029581022262573243, 0.03587849140167236, 0.042772865295410155, 0.04986958503723145]
#######################################################################################
def plot():
    plt.plot(nodes, greedy_without, 'bo', label = "Greedy without dependencies")
    plt.plot(nodes, greedy_with, 'r*', label = "Greedy with dependencies")
    plt.xlabel("Number of transactions")
    plt.ylabel("Runtime in seconds")
    plt.legend(loc = 'upper left')
    plt.show()
#######################################################################################