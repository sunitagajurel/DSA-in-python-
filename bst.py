class tree: 
    def __init__(self,key):
        self.key = key
        self.left_child = None
        self.right_child = None
    
    #visits root -->leftnode ---> rightnode
    def pre_order_traversal (self): 
        print(self.key,end =" ")
        if self.left_child: 
            self.left_child.pre_order_traversal()
        if self.right_child: 
            self.right_child.pre_order_traversal()

    #visits leftnode-->root -->rightnode     
    def in_order_traversal(self):
        if self.left_child: 
            self.left_child.in_order_traversal()
        print(self.key,end = " ")
        if self.right_child: 
            self.right_child.in_order_traversal()
    
    #visits rightnode-->root -->leftnode
    def post_order_traversal(self): 
        if self.right_child:
            self.right_child.post_order_traversal()
        print(self.key,end = " ")
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
                
    def delete_node(self,data,curr): 
        if self.key is None: 
            print("tree is empty")
            return 
        if data < self.key : 
            if self.left_child:
                self.left_child = self.left_child.delete_node(data,curr)
            else: 
                print("no node found")
        elif data >self.key: 
            if self.right_child: 
               self.right_child = self.right_child.delete_node(data,curr) 
            else: 
                print("no node found")
        else: 
            if self.left_child is None: 
                temp = self.right_child
                if data == curr: 
                    self.key = temp.key
                    self.right_child = temp.right_child
                    self.left_child = temp.left_child
                    temp = None
                    return

                self = None
                return temp

            if self.right_child is None: 
                temp = self.left_child
                if data == curr: 
                    self.key = temp.key
                    self.right_child = temp.right_child
                    self.left_child = temp.left_child
                    temp = None
                    return
                self = None
                return temp 

            node = self.right_child
            while node.left_child: 
                node = node.left_child
            self.key = node.key 
            self.right_child = self.right_child.delete_node(data,curr)
        return self

def count(node): 
    if node is None: 
        return 0 
    return 1+count(node.left_child) +count(node.right_child)      

root = tree(10)
list = [3,50,40,5,14]
for i in list: 
    root.insert_data(i)

print("no of node in tree is: ", count(root))
print("max value is :", root.find_max())
print("min value is :", root.find_min())
print(root.search_data(50))

root.pre_order_traversal()
if count(root) > 1: 
    root.delete_node(10,root.key)
else: 
    print("can't perform delete operation on node")
print("inorder traversal")
root.in_order_traversal()
print("postorder traversal")
root.post_order_traversal()
