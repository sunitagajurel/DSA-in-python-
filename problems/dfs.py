from ast import GtE


tree = [['A','B','c'],['D','E','F'],['G','H','I']]
for row in tree : 
    print(row)
startpos = (0,0)
goalpos= (1,1)

#for obtaining neighbour
offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def dfs (tree,start,goal):
    stack = [start] 
    visited = []
    full_path= []
    # result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    while stack: 
        current = stack.pop()
        print('stack is{}'.format(stack))
        full_path.append(current)
        visited.append(current)
        if current == goal:
            return full_path

        for direction in ["up", "right", "down","left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current[0]+row_offset,current[1]+col_offset) #calculating neigbour
            #checking if index is out of range 
            if neighbour[0]<3 and neighbour[0]>-1 and neighbour[1]<3 and neighbour[1]>-1 and neighbour not in visited:
                stack.append(neighbour)
                print('stack is{}'.format(stack))
print(dfs(tree,startpos,goalpos))






