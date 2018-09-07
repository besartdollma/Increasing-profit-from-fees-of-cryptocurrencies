import time
import matplotlib.pyplot as plt
import dependency knapsack solvers as dks
import createGraph

BLOCK_SIZE = 1000000 # 1 MB
#####################################################################################
def check_if_only_added(G1, G2):
    elements1 = set([x[0] for x in G1.nodes.data()])
    elements2 = set([x[0] for x in G2.nodes.data()])
    if (len(elements1.difference(elements2)) == 0):
        return True
    return False
#####################################################################################
def real_data(date):

    sample = []
    reg_time = []
    reg_sol_list = []
    inc_time = []
    inc_sol_list = []

    G1 = createGraph.create_graph(date, 1)
    last_sol = dks.get_set_greedy2(G1, BLOCK_SIZE)

    for i in range(1,26,1):
        print(i)
        sample.append(i)
        G2 = createGraph.create_graph(date, i+1)

        if not check_if_only_added(G1, G2):
            print("not increment")

        start = time.time()
        reg_sol_set = dks.get_set_greedy2(G2, BLOCK_SIZE)
        reg_sol = dks.fee_of_set(G2, reg_sol_set)
        end = time.time()

        reg_time.append(end-start)
        reg_sol_list.append(reg_sol)

        start = time.time()
        inc_sol = dks.get_fee_greedy_inc(G2, BLOCK_SIZE, last_sol)
        end = time.time()

        inc_time.append(end-start)
        inc_sol_list.append(inc_sol)

        G1 = G2
        last_sol = reg_sol_set

    print("sample = " + str(sample))
    print("reg_time = " + str(reg_time))
    print("reg_sol = " + str(reg_sol_list))
    print("inc_time = " + str(inc_time))
    print("inc_sol_list = " + str(inc_sol_list))

#####################################################################################
# DATA CREATED FROM THE PREVIOUS FUNCTION - DATE "28/08/2017" - TIME SAMPLE 1-25 - FIGURES 27-28
# sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# reg_time = [16.878549337387085, 17.481176376342773, 18.149763107299805, 17.926282167434692, 17.99885892868042, 17.618091344833374, 17.960882663726807, 17.93989372253418, 18.62326192855835, 18.96509027481079, 18.800790309906006, 18.543157815933228, 18.948272705078125, 18.874316692352295, 18.90329599380493, 18.96325922012329, 18.96226406097412, 18.97825026512146, 19.278196573257446, 19.15914273262024, 18.60548233985901, 18.79136872291565, 18.89130663871765, 19.153143644332886, 18.855341911315918]
# reg_sol = [1.5571744000000023, 1.5621531100000026, 1.5658302600000027, 1.574787010000003, 1.5789343600000032, 1.6124683400000035, 1.6204950400000038, 1.6282593800000031, 1.6452574600000034, 1.6642307600000035, 1.6710416300000033, 1.683168700000004, 1.6963972600000037, 1.735917980000004, 1.7510973700000039, 1.7616688500000037, 1.7758200700000033, 1.7807501800000036, 1.7928611000000039, 1.8022620400000033, 1.9012973900000034, 1.9099278300000029, 1.914134550000003, 1.9223995800000033, 1.9336303200000031]
# inc_time = [15.34150242805481, 16.14001178741455, 16.48179841041565, 15.25455641746521, 16.25893759727478, 16.61171793937683, 15.345501184463501, 16.25693655014038, 16.633354425430298, 16.973493576049805, 15.359731197357178, 16.33089256286621, 16.412848472595215, 17.021464824676514, 16.94650959968567, 17.147388458251953, 17.137393474578857, 16.263935089111328, 17.824968814849854, 16.11002826690674, 16.834579467773438, 16.06405520439148, 15.713273763656616, 17.12040138244629, 16.834580421447754]
# inc_sol_list = [1.5571744000000014, 1.5621531100000026, 1.5658302600000016, 1.574787010000002, 1.5789343600000032, 1.6124683400000013, 1.6205367600000011, 1.6282593800000011, 1.6452574600000014, 1.664230760000002, 1.6710416300000033, 1.683168700000004, 1.6963972600000021, 1.735917980000004, 1.7510973700000032, 1.7616688500000035, 1.775820070000002, 1.7807501800000034, 1.7928611000000017, 1.8022620400000013, 1.9012973900000034, 1.9099278300000009, 1.9141345500000013, 1.9223995800000016, 1.9336303200000013]
# #####################################################################################
# DATA CREATED FROM THE PREVIOUS FUNCTION - DATE "03/09/2017" - TIME SAMPLE 1-25 - FIGURES 29-30
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
reg_time = [0.8154935836791992, 0.945415735244751, 1.1922612190246582, 1.1932604312896729, 0.8904502391815186, 0.9494109153747559, 1.262218713760376, 0.8604674339294434, 1.5341768264770508, 0.9383208751678467, 0.7869205474853516, 1.4977741241455078, 1.1714751720428467, 1.7294073104858398, 0.9763953685760498, 1.0183682441711426, 1.4211182594299316, 1.1902623176574707, 1.0793330669403076, 1.3811452388763428, 1.1832671165466309, 0.9973812103271484, 0.9114346504211426, 0.9514114856719971, 0.8964457511901855]
reg_sol = [0.5814665299999981, 0.5877670499999982, 0.5874296299999981, 0.5874296299999981, 0.5874296299999981, 0.5874296299999981, 0.5874296299999981, 0.5874296299999981, 0.5874296299999981, 0.5889359499999982, 0.6581508299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6660572399999981, 0.6660572399999981, 0.6660572399999981, 0.6660572399999981, 0.6680708599999982, 0.6680708599999982, 0.6680708599999982]
inc_time = [0.8394804000854492, 0.9114346504211426, 1.0193674564361572, 0.5446617603302002, 0.5436630249023438, 0.5636518001556396, 0.7035722732543945, 0.5506591796875, 0.5260903835296631, 0.9325823783874512, 0.8504533767700195, 0.9202713966369629, 0.936997652053833, 0.7005672454833984, 0.506685733795166, 0.6785802841186523, 0.5186805725097656, 0.5826406478881836, 1.1372978687286377, 0.5716447830200195, 0.5706489086151123, 0.5396687984466553, 0.9124343395233154, 0.5156800746917725, 0.528672456741333]
inc_sol_list = [0.5814665299999991, 0.5877670499999991, 0.5874296299999981, 0.587429629999999, 0.587429629999999, 0.587429629999999, 0.587429629999999, 0.587429629999999, 0.587429629999999, 0.5889359499999982, 0.6581508299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.6583168299999979, 0.666057239999998, 0.666057239999998, 0.666057239999998, 0.666057239999998, 0.6680708599999982, 0.668070859999998, 0.668070859999998]
#####################################################################################
def plot3():
    plt.plot(sample, reg_time, 'bo', label="Non-incremental")
    plt.plot(sample, inc_time, 'r*', label='Incremental')
    plt.xlabel("Time - sample number")
    plt.ylabel("Running time in seconds")
    plt.legend(loc='upper left')
    plt.show()
#####################################################################################
def plot4():
    plt.plot(sample, reg_sol, 'bo', label="Non-incremental")
    plt.plot(sample , inc_sol_list, 'r*', label='Incremental')
    plt.xlabel("Time- sample number")
    plt.ylabel("Solution value")
    plt.legend(loc='upper left')
    plt.show()
#####################################################################################
