class tree: 
    def __init__(self,key):
        self.key = key
        self.left_child = None
        self.right_child = None
    

    def pre_order_traversal (self): 
        print(self.key)
        if self.left_child: 
            self.left_child.pre_order_traversal()
        if self.right_child: 
            self.right_child.pre_order_traversal()
            

    def in_order_traversal(self):
        return 

    def post_order_traversal(self): 
        return 

    def insert_data(self,data):
        if data <= self.key: 
            if self.left_child: 
                self.left_child.insert_data(data)
            else: 
                self.left_child = tree(data)
        else: 
            if self.right_child: 
                self.right_child.insert_data(data)
            else: 
                self.right_child = tree(data)
               
    def find_max(self):
        while self.right_child is not None: 
            self = self.right_child
        return self.key

    def find_min(self): 
        while self.left_child is not None: 
            self = self.left_child
        return self.key

    def search_data(self,data): 
        if data == self.key: 
                return "data found"

        if data > self.key: 
            if self.right_child: 
                self.right_child.search_data(data)
            else: 
                print("Node is not present in tree")
            
        else:
            if self.left_child: 
                return self.left_child.search_data(data)

            else:
                return "no node found"
                
    
    def delete_data(self): 
        return 

res = []
root = tree(10)
root.insert_data(5)
root.insert_data(25)
root.insert_data(15)
root.insert_data(6)
root.insert_data(2)

print(root.key)
print(root.left_child.key)
print(root.right_child.key)
print(root.left_child.left_child.key)
print(root.right_child.left_child.key)

print("max value is :", root.find_max())
print("min value is :", root.find_min())
print(root.search_data(50))

root.pre_order_traversal()



