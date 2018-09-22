import knapsack_solvers as ks
import networkx as nx
import random
import time
import matplotlib.pyplot as plt

AVERAGE_RUN = 50
BLOCK_SIZE = 1000
#######################################################################################
def create_random_graph(num_of_nodes, with_edges):
    G = nx.DiGraph()
    for i in range(num_of_nodes):
        G.add_node(i,size=random.randint(1,100),fee=random.randint(1,100))
    if with_edges:
        for i in range(num_of_nodes):
            G.add_edge(random.randint(0,num_of_nodes-1),random.randint(0,num_of_nodes-1))
    return G
#######################################################################################
def create_data():
    nodes = []
    exh = []
    exh_list = []
    dyn_prog = []
    dyn_prog_list = []
    greedy = []
    greedy_list = []
    eps = []
    eps_list = []

    for i in range(1,21):
        nodes.append(i)
        exh_sum = 0
        exh_sol = 0
        dyn_sum = 0
        dyn_sol = 0
        greedy_sum = 0
        greedy_sol = 0
        eps_sum = 0
        eps_sol =0

        for j in range(AVERAGE_RUN):
            G = create_random_graph(i, False)

            start = time.time()
            exh_sol += ks.exhaustive_search(G, BLOCK_SIZE)[0]
            end = time.time()
            exh_sum += end - start

            start = time.time()
            dyn_sol += ks.dynamic_prog(G, BLOCK_SIZE)
            end = time.time()
            dyn_sum += end - start

            start = time.time()
            greedy_sol += ks.greedy(G, BLOCK_SIZE)
            end = time.time()
            greedy_sum += end - start


            start = time.time()
            eps_sol += ks.greedy_epsilon(G, 0.5, BLOCK_SIZE,'fee')
            end = time.time()
            eps_sum += end - start

        exh.append(exh_sum/AVERAGE_RUN)
        exh_list.append(exh_sol/AVERAGE_RUN)
        dyn_prog.append(dyn_sum/AVERAGE_RUN)
        dyn_prog_list.append(dyn_sol/AVERAGE_RUN)
        greedy.append(greedy_sum/AVERAGE_RUN)
        greedy_list.append(greedy_sol/AVERAGE_RUN)
        eps.append(eps_sum/AVERAGE_RUN)
        eps_list.append(eps_sol/AVERAGE_RUN)


    print(nodes)
    print("exhaustive_time = " + str(exh))
    print("exhaustive_sol = " + str(exh_list))
    print("dynamic_time = " + str(dyn_prog))
    print("dynamic_sol = " + str(dyn_prog_list))
    print("greedy_time = " + str(greedy))
    print("greedy_sol =" + str(greedy_list))
    print("eps_05_time = " + str(eps))
    print("eps_05_sol =" + str(eps_list))

#######################################################################################
# THE DATA THAT THE PREVIOUS FUNCTION OUT PUTTED FIGURES 2-3
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
exhaustive_time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0003124856948852539, 0.0, 0.0009374666213989258, 0.0015624380111694336, 0.003437356948852539, 0.007187142372131348, 0.017187118530273438, 0.036248517036437986, 0.08218424797058105, 0.18124265670776368, 0.3952981424331665, 0.7668479585647583, 1.634632749557495, 3.5039463901519774, 7.7358380317687985]
exhaustive_sol = [52.96, 101.32, 158.66, 199.78, 249.44, 291.5, 359.32, 397.94, 455.34, 519.9, 548.74, 594.98, 649.4, 741.96, 746.92, 834.2, 859.88, 893.82, 967.24, 1014.78]
dynamic_time = [0.0006249523162841796, 0.00187497615814209, 0.0024999046325683595, 0.003437356948852539, 0.0037498760223388674, 0.004374856948852539, 0.006249790191650391, 0.00593724250793457, 0.007499771118164062, 0.00843721866607666, 0.010624780654907226, 0.01031193733215332, 0.01187488555908203, 0.011250133514404298, 0.01406334400177002, 0.01343808650970459, 0.013438282012939453, 0.015311970710754394, 0.01562302589416504, 0.015934815406799318]
dynamic_sol = [52.96, 101.32, 158.66, 199.78, 249.44, 291.5, 359.32, 397.94, 455.34, 519.9, 548.74, 594.98, 649.4, 741.96, 746.92, 834.2, 859.88, 893.82, 967.24, 1014.78]
greedy_time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006250333786010742, 0.0, 0.0, 0.0, 0.0]
greedy_sol = [52.96, 101.32, 158.66, 199.78, 249.44, 291.5, 359.32, 397.94, 455.34, 519.9, 548.74, 594.98, 649.4, 741.96, 746.62, 834.2, 859.78, 893.02, 966.8, 1013.6]
eps_05_time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0003125381469726563, 0.0, 0.00031252861022949217, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00031252384185791014, 0.0, 0.0, 0.00031246185302734374]
eps_05_sol =[52.96, 101.32, 158.66, 199.78, 249.44, 291.5, 359.32, 397.94, 455.34, 519.9, 548.74, 594.98, 649.4, 741.96, 746.62, 834.2, 859.78, 893.02, 966.8, 1013.6]
#######################################################################################
def plot1():
    plt.plot(nodes, exhaustive_time, 'bo', label = "Exhaustive Search")
    plt.plot(nodes, dynamic_time, 'k+', label = "Dynamic Programming", markersize='10')
    plt.plot(nodes, greedy_time, 'gx', label ='Greedy Approximation', markersize='7')
    plt.plot(nodes, eps_05_time, 'r*', label = "1+Eps, Eps=0.5" )
    plt.xlabel("Number of Transactions")
    plt.ylabel("Running time in seconds")
    plt.legend(loc='upper left')
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
    plt.plot(nodes, relative(dynamic_sol,exhaustive_sol),'k+', label = "Dynamic Programming", markersize='10')
    plt.plot(nodes, relative(greedy_sol,exhaustive_sol), 'gx', label ='Greedy Approximation', markersize='7')
    plt.plot(nodes, relative(eps_05_sol,exhaustive_sol), 'r*', label = "1+Eps, Eps=0.5" )
    plt.xlabel("Number of Transactions")
    plt.ylabel("Error relative to Optimal Solution")
    plt.legend(loc='upper left')
    plt.show()
#######################################################################################

