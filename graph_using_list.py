def insert_node(node):
    if node in graph: 
        print("edge already present")
    else:
        graph[node] = []


def add_edge(v1,v2,cost):
    if v1 not in graph: 
        print (f'vertex {v1} not found')
        return
    elif v2 not in graph: 
        print (f'vertex {v2} not found')
        return
    else:
        # list1 = [v2,cost] 
        # list2 = [v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1) #not needed if directed graph
    return graph

def del_node(node):
    if node not in graph: 
        print("node not found")
    else: 
        del graph[node]
        for i in graph:
            list1 = graph[i]
            for j in list1: 
                if node in j[0]:
                    list1.remove(j)
    return graph

def del_edge(v1,v2,cost):
    if v1 not in graph: 
        return (f'vertex {v1} not found')
    elif v2 not in graph: 
        return (f'vertex {v1} not found')
    else:
        #{A: [[b,2],[c,2]]} this should be used if you dont want to pass cost
        # for i in graph: 
        #     ith_node = graph[i]
        #     for j in ith_node: 
        #         if v1 == j[0] or v2 ==j[0]:
        #             ith_node.remove(j)

        temp = [v1,cost]
        temp1 = [v2,cost] 
        
        if temp1 in graph[v1]: #checks if v1 has edge to v2 -> v2 also has has edge to v1  -> removes v1 from the path of v2 and vice versa
            graph[v1].remove(temp1) 
            graph[v2].remove(temp)
    return graph

def dfs_traversal(node,visited,graph):
    if node not in graph: 
        print("node not in graph")
        return
    if node not in visited:
        visited.add(node)
        print(node,"-->",end = " ")
        for i in graph[node]:
            dfs_traversal(i,visited,graph)
    return 


def traversal_itr(start_node,graph):
    stack = []
    stack.append(start_node)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node,"-->",end = " ")
            adjacent_node = graph[node] 
            stack = stack+adjacent_node
            
    return


    
    

visited = set()
graph = {}
insert_node('A')
insert_node('B')
insert_node('C')
insert_node('D')
add_edge('A','B',5)
add_edge('A','C',5)
add_edge('C','D',5)
print(graph)
# del_edge('A','B',5)
# dfs_traversal('A',visited,graph)
traversal_itr('A',graph)
# print(graph)