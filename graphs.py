#function new node to graph using adjacncy matrix representation 
from operator import indexOf


def add_node(v):
    global node_count
    if v in nodes: 
        print("the node is already present in the graph")
    else: 
        node_count+= 1 
        nodes.append(v)
        #inserts one in each row [add one column in each row]  
        for n in graph: 
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

#adding an edge between the nodes in undirected 
#adds 1 for edge in unweighted , cost in weighted
def add_edge(v1,v2):
    if (v1 not in nodes):
        print(v1, "not present in graph")
    elif v2 not in nodes: 
        print(v1, "not present in graph")
    else:
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)
        graph[index_v1][index_v2] = 1
        graph[index_v2][index_v1] = 1 #not necessary in directed graph there will be direction from A-> B 
    return graph

    
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j]),end = "")
        print()

nodes = []
#adjacent matrix
graph = []
node_count = 0

print("before addingnodes,no.of node = ",node_count,nodes,graph)
add_node('A')
add_node('B')
print("after addingnodes,no.of node = ",node_count,nodes,graph)
add_edge('A','C')
add_edge('A','B')
print("after addingnodes,no.of node = ",node_count,nodes,graph)
print_graph()



