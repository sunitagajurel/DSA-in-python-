class Node():
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
    
    def inOrder(root):
        print(root)
        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right

            else:
               break

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
root.inOrder()



