class heap: 
    def __init__(self,key):
        self.key = key 
        self.left_child = None
        self.right_child = None
    
    #inserts making complete binary tree
    def insert(self,key):
        if self.left_child is None: 
            self.left_child = heap(key)
            return 
        
        if self.right_child is None: 
            self.right_child = heap(key)
        
        else: 
            self.left_child.insert(key)


    
    def heapify_up(self):
        # if self.key < self.left_child.key:
        #     temp = self.left_child.key 
        #     self.left_child.key = self.key 
        #     self.key = temp  

        # if self.key < self.right_child.key:
        #     temp = self.right_child.key 
        #     self.right_child.key = self.key 
        #     self.key = temp 
        return 

        

    def heapify_down(self):
        return 

    def delete_node(self,key): 
        return 

root = heap(10)
root.insert(4)
root.insert(6)
root.insert(5)

print(root.key)
print(root.left_child.key)
print(root.right_child.key)
print(root.left_child.left_child.key)