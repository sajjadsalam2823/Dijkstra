import csv
import math

def readlist_list(filename):
    """
        input: the name of the txt file
        output: a list of lists containing the element of the array 
        in the txt file
    """
    dicts = {}
    i_node = 1
    with open(filename, "rt", newline = '') as csv_file:
        csv_read = csv.reader(csv_file, delimiter='\t')
        for row in csv_read:
            row.pop()
            del row[0]
            temp_lst = []
            for entry in row:
                temp_lst.append((int(entry.split(',')[0]),int(entry.split(',')[1])))
            dicts[i_node] = temp_lst
            i_node += 1
            
        
    return dicts
    
def list_len(dict_node):
    """
    input: the dictionary generated in the last function
    output: a list of tuples which the first element is the number of node and
    second element is the len from source initialezed to infinity
    """
    dict_len = {}
    for key in dict_node.keys():
        if key == 1:
            dict_len[key] = 0
        else:
            dict_len[key] = math.inf        
    return dict_len
    
def Dijkstra(G, dict_):
    """
    computes the shortest path to every node from the source node which is 
    the first node
    
    input: the dictionaries returned by two previous functions
    output: a dictionary that have each node with len of shortest path to the 
    source node
    """
    lst_path = {}
    shortl = 0
    key_find = 0
# the range can be simply changed to n-1, when n is number of nodes
    for n in range(199):
        val_min = math.inf
        for key, val in dict_.items():
            if key not in lst_path.keys():
                if val < val_min: 
                    key_find = key
                    val_min = val
                    shortl = val
        for item in G[key_find]:
            if item[1] + shortl < dict_[item[0]]:
                dict_[item[0]] = item[1] + shortl

        if val_min == 0:
            lst_path[key_find] = dict_[1]
        else:
            lst_path[key_find] = dict_[key_find]
    return lst_path

def lst_shortpath(Dijkstra_dict):
    """
    input: the dictionary of shortest path to each node
    output: a list of shortest path for the desired list of nodes
    """
    lst = [7,37,59,82,99,115,133,165,188,197]
    output = []
    for entry in lst:
        output.append(Dijkstra_dict[entry])
    return output

G = readlist_list('data.txt')
dict_ = list_len(G)
print(lst_shortpath(Dijkstra(G, dict_)))    