import knapsack_solvers as ks
import networkx as nx
import random
import time
import matplotlib.pyplot as plt

BLOCK_SIZE = 1000
#######################################################################################
def create_random_graph(num_of_nodes, with_edges):
    G = nx.DiGraph()
    for i in range(num_of_nodes):
        G.add_node(i,size=random.randint(1,200),fee=random.randint(1,200))
    if with_edges:
        for i in range(num_of_nodes):
            G.add_edge(random.randint(0,num_of_nodes-1),random.randint(0,num_of_nodes-1))
    return G
#######################################################################################
def create_data():
    epsilon_list = []
    sol = []
    Time =[]
    G = create_random_graph(50, False)
    print(ks.greedy(G, BLOCK_SIZE))
    epsilon = 1
    while(epsilon>0.01):
        print(epsilon)
        start = time.time()
        sol.append(ks.greedy_epsilon(G, epsilon, BLOCK_SIZE, 'fee'))
        end = time.time()
        Time.append(end - start)
        epsilon_list.append(epsilon)
        epsilon*= 0.8

    print("epsilon_list = " + str(epsilon_list))
    print("Time = " + str(Time))
    print("Sol = " + str(sol))
#######################################################################################
# THE DATA WAS CREATED FROM THE PREVIOUS FUNCTION, FIGURES 10-11
epsilon_list = [1, 0.8, 0.6400000000000001, 0.5120000000000001, 0.40960000000000013, 0.32768000000000014,
                0.2621440000000001, 0.2097152000000001, 0.1677721600000001, 0.13421772800000006, 0.10737418240000006,
                0.08589934592000005, 0.06871947673600004, 0.054975581388800036, 0.043980465111040035,
                0.03518437208883203, 0.028147497671065627, 0.022517998136852502, 0.018014398509482003,
                0.014411518807585602, 0.011529215046068483]
Time = [0.0, 0.000997781753540039, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.09094381332397461, 7.022812366485596, 66.47102975845337, 64.1053147315979, 68.32032012939453,
        62.76939582824707, 64.74760484695435, 64.34271931648254, 61.999945402145386]
Sol = [2379, 2379, 2379, 2379, 2379, 2379, 2379, 2379, 2379, 2379, 2379, 2379, 2418, 2418, 2418, 2418, 2418, 2418, 2418,
       2418, 2418]
#######################################################################################
def plot1():
    plt.plot(epsilon_list, Time, 'b+')
    plt.xlabel("Epsilon")
    plt.ylabel("Runtime in seconds")
    plt.show()
#######################################################################################
def relative(sol, x):
    temp = []
    for i in range(len(sol)):
        temp.append(sol[i]-x)
    return temp
#######################################################################################
def plot2():
    plt.plot(epsilon_list, relative(Sol,2379), 'b+')
    plt.xlabel("Epsilon")
    plt.ylabel("Profit relative to the greedy approximation")
    plt.show()
#######################################################################################