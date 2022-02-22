class Node:
    def __init__(self, data):
    #   print("checking its call{}".format(data))
      self.left = None
      
      self.right = None
     
      self.data = data
      
# Insert Node
    def insert(self, data):
        if self.data:
            print("existing data is "+ str(self.data))
            print("chirako data is " + str(data))
            if data < self.data:
              if self.left is None:
                self.left = Node(data)
                print("sano")
              else:
               print("something in left {}".format(self.left.data))
               self.left.insert(data)
               
            elif data > self.data:
                if self.right is None:
                  self.right = Node(data)
                  print("thulo")
                else:
                  print("something in right {}".format(self.right.data))
                  self.right.insert(data)
        else:
            print("ghh")
            self.data = data
            
# Print the Tree
    def PrintTree(self):
        if self.left:
          self.left.PrintTree()
        if self.right:
         self.right.PrintTree()
    

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
        #    print(root.data)
           res = self.inorderTraversal(root.left)
           res.append(root.data)
           print(res)
           res = res + self.inorderTraversal(root.right)
        return res
root = Node(27)
root.insert(5)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(9)
root.insert(11)
root.insert(31)
root.insert(42)

print(root.inorderTraversal(root))