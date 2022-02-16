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
        if self.left_child: 
            self.left_child.in_order_traversal()
        print(self.key)
        if self.right_child: 
            self.right_child.in_order_traversal()

    def post_order_traversal(self): 
        if self.right_child:
            self.right_child.post_order_traversal()
        print(self.key)
        if self.left_child: 
            self.left_child.post_order_traversal()

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
                
    
    def delete_node(self,data): 
        if self.key is None: 
            print("tree is empty")
            return 
        if data < self.key : 
            if self.left_child:
                self.left_child = self.left_child.delete_node(data)
            else: 
                print("no node found")
        elif data >self.key: 
            if self.right_child: 
               self.right_child = self.right_child.delete_node(data) 
            else: 
                print("no node found")
        else: 
            if self.left_child is None: 
                temp = self.right_child
                self = None
                return temp

            if self.right_child is None: 
                temp = self.left_child
                self = None
                return temp 

            node = self.right_child
            while node.left_child: 
                node = node.left_child
            self.key = node.key 
            self.right_child = self.right_child.delete_node(data)
        return self



    def delete(self,data): 
        if self.key is None: 
            print("node is empty")
            return 
        if self.key < data: 
            if self.left_child: 
              self.left_child = self.left_child.delete(data)
            else: 
                print("no data found")
        if self.key > data: 
            if self.right_child:
                self.right_child = self.right_child.delete(data)
            else: 
                print("no data found")
        else: 
            if  self.left_child is None: 
                temp = self.right_child
                self = None 
                return temp

            if self.right_child is None: 
                temp = self.left_child
                self = None 
                return temp 

            node = self.right_child
            while node.left_child:
                node = node.left_child 
            self.key = node.key 
            self.right_child = self.right_child.delete(node.key)
            return self




        


root = tree(10)
root.insert_data(5)
root.insert_data(25)
root.insert_data(15)
root.insert_data(6)
root.insert_data(2)

# print(root.key)
# print(root.left_child.key)
# print(root.right_child.key)
# print(root.left_child.left_child.key)
# print(root.right_child.left_child.key)

print("max value is :", root.find_max())
print("min value is :", root.find_min())
print(root.search_data(50))

root.pre_order_traversal()
root.delete_node(15)
print("inorder traversal")
root.in_order_traversal()
print("postorder traversal")
root.post_order_traversal()




