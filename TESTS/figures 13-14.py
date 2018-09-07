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
        G.add_node(i,size=random.randint(100,200),fee=random.randint(1,100))
    if with_edges:
        number_of_edges = random.randint(1,num_of_nodes)
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
    greedy = []
    greedy_list = []
    eps05 = []
    eps05_list = []
    eps003 = []
    eps003_list = []

    for i in range(1,150,5):
        print(i)
        nodes.append(i)
        greedy_sum = 0
        greedy_sol = 0
        eps05_sum = 0
        eps05_sol =0
        eps003_sum = 0
        eps003_sol = 0

        for j in range(AVERAGE_RUN):
            G = create_random_graph(i, True)
            print("created graph")

            start = time.time()
            greedy_sol += dks.get_fee_greedy2(G, BLOCK_SIZE)
            end = time.time()
            greedy_sum += end - start

            start = time.time()
            eps05_sol += dks.get_fee_generalized_greedy(G, 0.5, BLOCK_SIZE)
            end = time.time()
            eps05_sum += end - start

            start = time.time()
            eps003_sol += dks.get_fee_generalized_greedy(G, 0.03, BLOCK_SIZE)
            end = time.time()
            eps003_sum += end - start


        greedy.append(greedy_sum/AVERAGE_RUN)
        greedy_list.append(greedy_sol/AVERAGE_RUN)
        eps05.append(eps05_sum/AVERAGE_RUN)
        eps05_list.append(eps05_sol/AVERAGE_RUN)
        eps003.append(eps003_sum / AVERAGE_RUN)
        eps003_list.append(eps003_sol / AVERAGE_RUN)

    print("nodes = " + str(nodes))
    print("greedy_time = " + str(greedy))
    print("greedy_sol = " + str(greedy_list))
    print("eps05_time = " + str(eps05))
    print("eps05_sol = " + str(eps05_list))
    print("eps003_time = " + str(eps003))
    print("eps003_sol = " + str(eps003_list))

#######################################################################################
# DATA CREATED FROM PREVIOUS FUNCTION FIGURES 13-14
nodes = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141]
greedy_time = [0.0, 0.0, 0.001562190055847168, 0.009374761581420898, 0.003641080856323242, 0.0, 0.0015625, 0.004687190055847168, 0.004687094688415527, 0.00625004768371582, 0.007812237739562989, 0.0078116655349731445, 0.0078122615814208984, 0.00625004768371582, 0.00781261920928955]
greedy_sol = [56.7, 579.2, 1038.2, 1582.0, 1993.0, 2575.3, 3012.5, 3580.9, 3863.8, 4010.9, 4270.6, 4523.5, 4567.6, 4761.4, 4851.9]
eps05_time = [0.0, 0.0, 0.0015621423721313477, 0.0, 0.0015625, 0.009375286102294923, 0.0062498807907104496, 0.004687452316284179, 0.0046874284744262695, 0.00468747615814209, 0.006249737739562988, 0.006249928474426269, 0.009374523162841797, 0.009374523162841797, 0.009374618530273438]
eps05_sol = [56.7, 579.2, 1038.2, 1582.0, 1993.0, 2575.3, 3012.5, 3580.9, 3863.8, 4010.9, 4270.6, 4523.5, 4567.6, 4761.4, 4851.9]
eps003_time = [0.0, 0.02812371253967285, 2.9319636106491087, 9.185303258895875, 24.909952783584593, 18.576693773269653, 0.9869274854660034, 0.0078121662139892575, 0.007812404632568359, 0.009374141693115234, 0.007812213897705078, 0.007812595367431641, 0.00937495231628418, 0.006249928474426269, 0.006249427795410156]
eps003_sol = [56.7, 579.2, 1038.2, 1582.0, 1993.0, 2575.3, 3012.5, 3580.9, 3863.8, 4010.9, 4270.6, 4523.5, 4567.6, 4761.4, 4851.9]
#######################################################################################
def plot1():
    plt.plot(nodes, greedy_time, 'gx', label = "Greedy Approximation", markersize = '10')
    plt.plot(nodes, eps05_time, 'bo', label ='1+Eps, Eps=0.5')
    plt.plot(nodes, eps003_time, 'r*', label = "1+Eps, Eps=0.03")
    plt.xlabel("Number of Transactions")
    plt.ylabel("Running time in seconds")
    plt.legend(loc='upper right')
    plt.show()
#######################################################################################
def relative(sol, opt):
    rel = []
    for i in range(len(sol)):
        rel.append(opt[i]-sol[i])
    print(rel)
    return rel
#######################################################################################
def plot2():
    plt.plot(nodes, relative(greedy_sol,eps05_sol), 'bo', label ='1+Eps, Eps=0.5')
    plt.plot(nodes, relative(greedy_sol,eps003_sol), 'r*', label = "1+Eps, Eps=0.03")
    plt.xlabel("Number of Transactions")
    plt.ylabel("Profit relative to the greedy approximation")
    plt.legend(loc='upper left')
    plt.show()
#######################################################################################