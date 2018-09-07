import knapsack solvers as ks
import networkx as nx
import random
import time
import matplotlib.pyplot as plt

AVERAGE_RUN = 25
BLOCK_SIZE = 1000000
#######################################################################################
def create_random_graph(num_of_nodes, with_edges):
    G = nx.DiGraph()
    for i in range(num_of_nodes):
        G.add_node(i,size=random.randint(1,500),fee=random.randint(1,2000))
    if with_edges:
        for i in range(num_of_nodes):
            G.add_edge(random.randint(0,num_of_nodes-1),random.randint(0,num_of_nodes-1))
    return G
#######################################################################################
def create_data():

    nodes = []
    exh_search = []
    exh_search_list =[]
    dyn_prog = []
    dyn_prog_list = []
    greedy = []
    greedy_list = []
    eps = []
    eps_list = []

    for i in range(1,26):

        nodes.append(i)
        dyn_sum = 0
        dyn_sol = 0
        greedy_sum = 0
        greedy_sol = 0
        eps_sum = 0
        eps_sol =0

        for j in range(AVERAGE_RUN):
            G = create_random_graph(i, False)

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


        dyn_prog.append(dyn_sum/AVERAGE_RUN)
        dyn_prog_list.append(dyn_sol/AVERAGE_RUN)
        greedy.append(greedy_sum/AVERAGE_RUN)
        greedy_list.append(greedy_sol/AVERAGE_RUN)
        eps.append(eps_sum/AVERAGE_RUN)
        eps_list.append(eps_sol/AVERAGE_RUN)


    print("nodes = " + str(nodes))
    print("dynamic_time = " + str(dyn_prog))
    print("dynamic_sol = " + str(dyn_prog_list))
    print("greedy_time = " + str(greedy))
    print("greedy_sol = " + str(greedy_list))
    print("eps_05_time = " + str(eps))
    print("eps_05_sol = " + str(eps_list))
#######################################################################################
# # PREVIOUS FUNCTION OUTPUT FIGURES 4-5
# nodes = [1, 26, 51, 76, 101, 126, 151, 176, 201, 226, 251, 276, 301, 326, 351, 376, 401, 426, 451, 476, 501, 526, 551, 576, 601, 626, 651, 676, 701, 726, 751, 776, 801, 826, 851, 876, 901, 926, 951, 976]
# dynamic_time = [0.0009375429153442383, 0.024688830375671388, 0.05687792778015137, 0.07656652927398681, 0.10031755924224854, 0.1278190565109253, 0.1581331968307495, 0.17438396453857422, 0.2050103187561035, 0.2253235673904419, 0.24594972610473634, 0.27063836574554445, 0.30657766342163084, 0.3331408739089966, 0.35689268112182615, 0.41033330440521243, 0.4172082090377808, 0.4456471014022827, 0.46283554553985595, 0.494087495803833, 0.5294018745422363, 0.5406520414352417, 0.5797163724899292, 0.6062806749343872, 0.6244059467315674, 0.6606574630737305, 0.6878466796875, 0.7006601095199585, 0.7409744882583618, 0.776600546836853, 0.7944150304794312, 0.819415831565857, 0.8816063880920411, 0.9354813432693482, 0.9091133356094361, 0.9395242691040039, 0.978799376487732, 1.0050498580932616, 1.0309885787963866, 1.0378641653060914]
# greedy_time =  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0006250429153442383, 0.0, 0.0003125572204589844, 0.0, 0.0, 0.00031255245208740236, 0.0, 0.00031262874603271484, 0.00031261444091796876, 0.00031260967254638673, 0.0, 0.0003126001358032227, 0.0009376716613769532, 0.0003126192092895508, 0.0, 0.0009376621246337891, 0.00031263351440429687, 0.001875448226928711, 0.0003125953674316406, 0.0, 0.0003125810623168945, 0.001250624656677246, 0.0009378528594970703, 0.0009379148483276367, 0.0003126621246337891, 0.0, 0.00031250953674316406, 0.0003125429153442383, 0.0018978786468505859, 0.0010378599166870118, 0.0003225421905517578, 0.0006252050399780274, 0.0015630149841308594, 0.0003125953674316406, 0.00031256675720214844]
# eps_05_time = [0.0, 0.0003125143051147461, 0.0, 0.0003124856948852539, 0.00031246185302734374, 0.000937652587890625, 0.0, 0.00031250476837158203, 0.0012503480911254883, 0.0018753623962402344, 0.0012502336502075195, 0.0012502622604370116, 0.0009378433227539062, 0.0015632104873657226, 0.0015628004074096679, 0.0009379386901855469, 0.0025005865097045897, 0.004063262939453125, 0.0015628957748413086, 0.0015629673004150392, 0.0018753957748413085, 0.0015629005432128906, 0.0028131771087646484, 0.0025006914138793945, 0.0018754100799560547, 0.0034381103515625, 0.0018754100799560547, 0.003438401222229004, 0.0031260061264038086, 0.005626506805419922, 0.0015627241134643555, 0.004689011573791504, 0.004688849449157715, 0.0035985517501831055, 0.006499552726745605, 0.003498587608337402, 0.004063401222229004, 0.005313858985900879, 0.005314569473266601, 0.0068768739700317385]
# dynamic_sol = [57.32, 1218.08, 1811.92, 2281.54, 2556.78, 2890.3, 3177.92, 3424.08, 3682.48, 3811.36, 4037.18, 4258.9, 4394.74, 4596.16, 4756.56, 4938.02, 5034.8, 5195.06, 5356.78, 5519.78, 5713.64, 5743.82, 5963.92, 6079.08, 6173.96, 6385.18, 6537.54, 6611.6, 6689.64, 6798.86, 6978.06, 7034.6, 7165.28, 7321.6, 7349.3, 7610.12, 7568.84, 7778.96, 7765.26, 7839.14]
# greedy_sol = [57.32, 1208.78, 1790.44, 2248.32, 2522.44, 2866.04, 3144.68, 3393.34, 3649.78, 3774.82, 4007.3, 4228.0, 4359.98, 4565.28, 4727.0, 4901.36, 5004.48, 5160.28, 5320.58, 5497.42, 5675.0, 5710.28, 5928.2, 6044.74, 6142.82, 6349.64, 6500.3, 6580.08, 6653.5, 6763.5, 6945.06, 7007.28, 7131.8, 7284.4, 7313.44, 7580.66, 7539.14, 7748.12, 7730.18, 7805.86]
# eps_05_sol = [57.32, 1208.78, 1790.44, 2248.32, 2522.44, 2866.04, 3144.68, 3393.34, 3649.78, 3774.82, 4007.3, 4228.0, 4359.98, 4565.28, 4727.0, 4901.36, 5004.48, 5160.28, 5320.58, 5497.42, 5675.0, 5710.28, 5928.2, 6044.74, 6142.82, 6349.64, 6500.3, 6580.08, 6653.5, 6763.5, 6945.06, 7007.28, 7131.8, 7284.4, 7313.44, 7580.66, 7539.14, 7748.12, 7730.18, 7805.86]
# #######################################################################################
# PREVIOUS FUNCTION OUTPUT FIGURE 6
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
dynamic_time = [1.1386550521850587, 2.230939073562622, 3.1652408504486083, 4.211952743530273, 4.805505962371826, 5.773706493377685, 6.765972337722778, 7.642912015914917, 8.676749286651612, 9.563320770263672, 11.637597160339356, 12.418430376052857, 12.391810150146485, 13.29677001953125, 14.263411798477172, 15.366249151229859, 16.152322731018067, 17.14666892051697, 18.0158890914917, 18.989406566619873, 19.960765190124512, 20.814676971435546, 22.057707366943358, 22.654138584136962, 23.579006052017213]
dynamic_sol = [1014.44, 1680.36, 2845.84, 4397.4, 4770.8, 6618.48, 6957.4, 8090.76, 9479.16, 9801.84, 11019.88, 12234.4, 12977.72, 14354.72, 14539.96, 16301.64, 16699.68, 17659.0, 18535.52, 20324.16, 20472.92, 21769.08, 22901.4, 24690.32, 24863.6]
greedy_time = [7.99083709716797e-05, 0.0, 4.001617431640625e-05, 8.00323486328125e-05, 7.971763610839844e-05, 0.0, 7.989883422851563e-05, 0.0001199626922607422, 4.008293151855469e-05, 7.998466491699219e-05, 7.99560546875e-05, 3.993988037109375e-05, 7.992744445800781e-05, 3.994941711425781e-05, 0.0, 8.002281188964843e-05, 7.992744445800781e-05, 0.00011988639831542968, 7.989883422851563e-05, 0.00016003608703613281, 0.00019978523254394532, 0.00011993408203125, 3.997802734375e-05, 3.997802734375e-05, 7.993698120117187e-05]
greedy_sol = [1014.44, 1680.36, 2845.84, 4397.4, 4770.8, 6618.48, 6957.4, 8090.76, 9479.16, 9801.84, 11019.88, 12234.4, 12977.72, 14354.72, 14539.96, 16301.64, 16699.68, 17659.0, 18535.52, 20324.16, 20472.92, 21769.08, 22901.4, 24690.32, 24863.6]
eps_05_time = [0.00012004852294921875, 7.994651794433594e-05, 0.0, 0.00027994155883789064, 0.00011986732482910156, 7.99560546875e-05, 7.992744445800781e-05, 4.003524780273437e-05, 0.00012004852294921875, 3.993988037109375e-05, 8.000373840332031e-05, 0.00012007713317871093, 7.993698120117187e-05, 0.00024003982543945311, 0.00011991500854492187, 0.00011995315551757813, 7.993698120117187e-05, 0.0001998138427734375, 0.000159912109375, 0.0, 4.000663757324219e-05, 0.0, 0.00012001991271972656, 0.00011979103088378906, 0.00019988059997558594]
eps_05_sol = [1014.44, 1680.36, 2845.84, 4397.4, 4770.8, 6618.48, 6957.4, 8090.76, 9479.16, 9801.84, 11019.88, 12234.4, 12977.72, 14354.72, 14539.96, 16301.64, 16699.68, 17659.0, 18535.52, 20324.16, 20472.92, 21769.08, 22901.4, 24690.32, 24863.6]
#######################################################################################
def plot1():
    plt.plot(nodes, dynamic_time, 'k+', label ="Dynamic Programming")
    plt.plot(nodes, greedy_time, 'gx', label ='Greedy Approximation', markersize='7')
    plt.plot(nodes, eps_05_time, 'r*', label = "1+Eps, Eps=0.5")
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
    plt.plot(nodes, relative(dynamic_sol,dynamic_sol), 'k+', label = "Dynamic Programming")
    plt.plot(nodes, relative(greedy_sol,dynamic_sol), 'gx', label ='Greedy Approximation', markersize='7')
    plt.plot(nodes, relative(eps_05_sol,dynamic_sol), 'r*', label = "1+Eps, Eps=0.5")
    plt.xlabel("Number of Transactions")
    plt.ylabel("Error relative to Optimal Solution")
    plt.legend(loc='center right')
    plt.show()
#######################################################################################