import dependency knapsack solvers as dks
import createGraph
import matplotlib.pyplot as plt
import time

BLOCK_SIZE = 1000000
TIME_TEMPLATE = "28/08/2017"
TIME_SAMPLES= ["28/08/2017", "30/08/2017","03/09/2017",  "06/09/2017", "26/09/2017"]
EPSILON = [0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1]
##########################################################################################
def relative(sol, x, first):
    temp = []
    for i in range(len(sol)):
        if first:
            temp.append(x-sol[i])
        else:
            temp.append(sol[i]-x)
    return temp
##########################################################################################
# Graph Y=fee, X=epsilon , generalized_greedy
def createGraph1(t, sample_number):

    G = createGraph.create_graph(t, sample_number)
    start_g = time.time()
    greedy_sol = dks.get_fee_greedy2(G, BLOCK_SIZE)
    end_g = time.time()
    time_g = end_g - start_g
    fee=[]
    epsilon=[]
    times = []
    greedy_time = []
    for x in EPSILON:
        print("epsilon is " + str(x))
        epsilon.append(x)
        start = time.time()
        sol = dks.get_fee_generalized_greedy(G,x,BLOCK_SIZE)
        end = time.time()
        times.append(end-start)
        fee.append(sol)

    print("Epsilon =" + str(epsilon))
    print("Fee = " + str(fee))
    print("Time = " + str(times))
    print("greedy_sol =" + str(greedy_sol))
    print("time_g = " + str(time_g))
##########################################################################################
# DATA FROM create_graph1 FIGURES 15-16
time_g = 21.43773341178894
greedy_sol = 1.5504391
Epsilon = [0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1]
Fee = [1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391, 1.5504391,
           1.5504391]
Time = [15329.218672513962, 130.59225344657898, 16.8597149848938, 16.617419242858887, 16.468960523605347,
            16.538377285003662, 16.516560077667236, 16.380211114883423, 16.252402782440186, 16.298113584518433,
            21.03930974006653]

#########################################################################################
#FIGURE 15
def plot1():
    plt.plot(Epsilon, relative(Fee, greedy_sol, True), 'b+')
    plt.xlabel("Epsilon")
    plt.ylabel("Profit relative to the greedy approximation")
    plt.show()
#########################################################################################
#FIGURE 16
def plot2():
    greedy_time = []
    for i in range(len(Epsilon)):
        greedy_time.append(time_g)
    plt.plot(Epsilon, greedy_time, 'ro')
    plt.plot(Epsilon, Time, 'b+')
    plt.xlabel("Epsilon")
    plt.ylabel("Running time")
    plt.show()
##########################################################################################
# Graph Y=fee, X=day, both greedy and generalized greedy
def createGraph2(time_samples, sample_number):
    greedy_fees = []
    greedy_time = []
    generalized_fees =[]
    generalized_time = []
    for t in time_samples:
        print(t)
        G = createGraph.create_graph(t, sample_number)
        start = time.time()
        greedy_fees.append(dks.get_fee_greedy2(G, BLOCK_SIZE))
        end = time.time()
        greedy_time.append(end - start)
        start = time.time()
        generalized_fees.append(dks.get_fee_generalized_greedy(G,0.1,BLOCK_SIZE))
        end = time.time()
        generalized_time.append(end - start)

    print("TIME_SAMPLES = " + str(time_samples))
    print("greedy_sol = " + str(greedy_fees))
    print("greedy_time = " + str(greedy_time))
    print("epsilon1_sol = " + str(generalized_fees))
    print("epsilon1_time = " + str(generalized_time))

##########################################################################################
def number_of_nodes_per_day(time_samples,sample_number):
    nodes = []
    for t in time_samples:
        print(t)
        G = createGraph.create_graph(t, sample_number)
        nodes.append(G.number_of_nodes())
    print("nodes = " + str(nodes))
##########################################################################################
greedy_sol_day = [1.5504391, 2.67404308, 0.574663729, 1.062441439, 1.773842729]
greedy_time_day = [15.279527425765991, 20.81810998916626, 0.8124985694885254, 5.841382741928101, 8.060010194778442]
epsilon_sol_day= [1.5504391, 2.67404308, 0.574663729, 1.062441439, 1.773842729]
epsilon_time_day = [131.3935387134552, 90.73183631896973, 1394.550568819046, 13.368727445602417, 38.85694932937622]
nodes = [15685, 15298, 1972, 5191, 7637]
VaC = [3, 2, 13, 1, 2]
epsilon1_sol_day = [1.5504391000000006, 2.6740430800000046, 0.574663729999999, 1.0624414399999975, 1.7738427299999957]
epsilon1_time_day = [16.61695098876953, 22.354570627212524, 1.0155930519104004, 6.407537937164307, 8.864908456802368]
##########################################################################################
#FIGURE 17
def plot4(time_samples):
    plt.plot(time_samples, nodes, 'b+')
    plt.xlabel("Day")
    plt.ylabel("Number of transactions")
    plt.show()
##########################################################################################
# FIGURE 18
def plot5(time_samples):
    plt.plot(time_samples, greedy_sol_day, 'ro', label = 'Greedy Approximation')
    plt.plot(time_samples, epsilon1_sol_day, 'b+' , label = '1+Eps, Eps = 0.1' )
    plt.xlabel("Day")
    plt.ylabel("Solution Value")
    plt.legend(loc = 'upper right')
    plt.show()
##########################################################################################
# FIGURE 19
def plot6(time_samples):
    plt.plot(time_samples, greedy_time_day, 'ro', label = 'Greedy Approximation' )
    plt.plot(time_samples, epsilon1_time_day, 'b+' ,label = '1+Eps, Eps = 0.1')
    plt.xlabel("Day")
    plt.ylabel("Runtime in Seconds")
    plt.legend(loc = 'upper right')
    plt.show()
##########################################################################################
# FIGURE 20
def plot7(time_samples):
    plt.plot(time_samples, VaC, 'b+')
    plt.xlabel("Day")
    plt.ylabel("Size of the set VaC")
    plt.show()
##########################################################################################
# FIGURE 21
def plot8(time_samples):
    plt.plot(time_samples, greedy_sol_day, 'ro', label = 'Greedy Approximation')
    plt.plot(time_samples, epsilon_sol_day, 'b+', label = '1+Eps, Eps = 0.03')
    plt.xlabel("Day")
    plt.ylabel("Solution Value")
    plt.legend(loc = 'upper right')
    plt.show()
##########################################################################################
# FIGURE 22
def plot9(time_samples):
    plt.plot(time_samples, greedy_time_day, 'ro', label = 'Greedy Approximation' )
    plt.plot(time_samples, epsilon_time_day, 'b+', label = '1+Eps, Eps = 0.03')
    plt.xlabel("Day")
    plt.ylabel("Runtime in Seconds")
    plt.legend(loc = 'upper right')
    plt.show()

##########################################################################################
# FIGURE 23
def createGraph5(date):
    samples=[]
    sol=[]
    for i in range(10):
        G = createGraph.create_graph(date, i)
        samples.append(i)
        sol.append(dks.get_fee_greedy2(G, BLOCK_SIZE))

    print(samples)
    print(sol)

    plt.plot(samples, sol, 'b+')
    plt.xlabel("Sample number")
    plt.ylabel("Solution value")
    plt.show()

    samples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sol = [1.5397622700000009, 1.550439100000001, 1.5571744000000014, 1.5621531100000015, 1.5658302600000022,
     1.5747870100000025, 1.5789343600000023, 1.612468340000002, 1.6204950400000016, 1.6282593800000018]

##########################################################################################
