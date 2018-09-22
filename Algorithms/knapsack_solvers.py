import networkx as nx
import random
import itertools
from functools import lru_cache

max_set_size = 20

##################################################################################################
#@lru_cache()
#Returns all the subsets of the set that it receives as "iterable" that their size is 
# is smaller or equal to "size"
def get_subsets_smaller_than_size(iterable, size):
    s = list(iterable)
    return itertools.chain.from_iterable\
        (itertools.combinations(s, r) for
         r in range(size+1))

##################################################################################################
def create_graph(elements):
    G = nx.DiGraph()
    for i in range(len(elements)):
        G.add_node(elements[i][0], size=elements[i][1]['size'], fee=elements[i][1]['fee'])

    return G
##################################################################################################
# Dynamic programming algorithm. Returns only the solution value.
@lru_cache()
def dynamic_prog(G, block_size):

    elements = list(G.nodes.data())
    num_of_elements = G.number_of_nodes()
    matrix = [[0 for x in range(block_size+1)] for y in range(num_of_elements+1)]
    for k in range(1,num_of_elements+1):
        for w in range(1,block_size+1):
            w_k = elements[k-1][1]['size']
            p_k = elements[k-1][1]['fee']
            if w_k > w:
                matrix[k][w] = matrix [k-1][w]
            else:
                matrix[k][w] = max(matrix[k-1][w],p_k + matrix[k-1][w-w_k])

    return matrix[num_of_elements][block_size]

##################################################################################################
# Greedy approximation algorithm, returns only the solution value.
@lru_cache()
def greedy(G,block_size):
    elements = list(G.nodes.data())
    num_of_elements = G.number_of_nodes()
    elements = sorted(elements,key=lambda node: (node[1]['fee'])/(node[1]['size']),reverse=True)
    current_weight = 0
    current_cost = 0
    for k in range(num_of_elements):
        if current_weight + elements[k][1]['size'] > block_size:
            if elements[k][1]['size'] <= block_size:
                return max(current_cost,elements[k][1]['fee'])
            return current_cost
        current_cost += elements[k][1]['fee']
        current_weight += elements[k][1]['size']

    return current_cost
##################################################################################################
# (1+epsilon) approximation algorithm. Returns only the solution value.
@lru_cache()
def greedy_epsilon(G, epsilon, block_size, reduction_param):

    greedy.cache_clear()
    greedy_solution = greedy(G,block_size)
    a = epsilon*greedy_solution
    elements = list(G.nodes.data())
    smaller_than_a = [e for e in elements if e[1]['fee']<a]
    greater_than_a = [e for e in elements if e[1]['fee']>=a]
    if(len(greater_than_a) > max_set_size):
        greater_than_a = reduce_sets(smaller_than_a,greater_than_a, reduction_param)
    weight_of_smaller_than_a = sum(map(lambda el: int(el[1]['size']), list(smaller_than_a)))
    cost_of_smaller_than_a = sum(map(lambda el: int(el[1]['fee']), list(smaller_than_a)))
    all_subsets = list(get_subsets_smaller_than_size(greater_than_a,min(int(2/epsilon),len(greater_than_a))))
    best_value = 0
    for subset in all_subsets:
        cost_of_subset = sum(map(lambda el: int(el[1]['fee']), list(subset)))
        weight_of_subset = sum(map(lambda el: int(el[1]['size']), list(subset)))
        if weight_of_subset > block_size:
            continue
        if weight_of_smaller_than_a + weight_of_subset <= block_size:
            best_value = max(best_value,cost_of_subset+cost_of_smaller_than_a)
            continue
        greedy_smaller_than_a = greedy(create_graph(smaller_than_a),block_size-weight_of_subset)
        best_value = max(best_value,cost_of_subset+greedy_smaller_than_a)

    return best_value

##################################################################################################
# Recudes the bigger_set to "max size" (defined at top). The rest of the elements are 
# moved to smaller_set. The reduction is done according to par.
def reduce_sets(smaller_set,bigger_set,par):

    if par == "relation":
        bigger_set = sorted(bigger_set, key=lambda node: (node[1]['fee']) / (node[1]['fee']), reverse=True)
    elif par == "random" :
        random.shuffle(bigger_set)
    elif par == "fee":
        bigger_set = sorted(bigger_set, key=lambda node: (node[1]['fee']), reverse=True)
    elif par == "size":
        bigger_set = sorted(bigger_set, key=lambda node:  (node[1]['size']), reverse=False)
    for x in bigger_set[max_set_size:]:
        smaller_set.append(x)

    return bigger_set[:max_set_size]


##################################################################################################
# Exhaustive search algorithm. Returns a tuple of (cost, weight) of the optimal solution.
@lru_cache()
def exhaustive_search(G, block_size):
    cost = 0
    weight = 0
    elements = list(G.nodes.data())
    all_subsets = list(get_subsets_smaller_than_size(elements,len(elements)))
    for subset in all_subsets:
        cost_of_subset = sum(map(lambda el: int(el[1]['fee']),list(subset)))
        weight_of_subset = sum(map(lambda el: int(el[1]['size']), list(subset)))
        if weight_of_subset <= block_size:
            if cost < cost_of_subset:
                cost = cost_of_subset
                weight = weight_of_subset

    return cost,weight

##################################################################################################

