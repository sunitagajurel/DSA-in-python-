#function new node to graph using adjacncy matrix representation 
def add_node(v):
    global node_count
    if v in nodes: 
        print("the node is already present in the graph")
    else: 
        node_count+= 1 
        nodes.append(v)
        #inserts in each column 
        for n in graph: 
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end = "")
        print()

nodes = []
#adjacent matrix
graph = []
node_count = 0

print("before addingnodes,no.of node = ",node_count,nodes)
add_node('A')
add_node('B')
print("after addingnodes,no.of node = ",node_count,nodes)
print_graph()



