class heap: 
    def __init__(self,key):
        self.key = key 
        self.left_child = None
        self.right_child = None
    
    #inserts making complete binary tree
    def insert(self,key):  #1,2,3,4,5,6,7
        if self.left_child is None: 
            self.left_child = heap(key)
            return 
        
        if self.right_child is None: 
            self.right_child = heap(key)
            return 

        if self.left_child.left_child  and self.left_child.right_child:
            print("new layer")
            self.right_child.insert(key)
            return 
        else: 
            self.left_child.insert(key)

    def pre_order_traversal (self): 
        print(self.key,end =" ")
        if self.left_child: 
            self.left_child.pre_order_traversal()
        if self.right_child: 
            self.right_child.pre_order_traversal()
        
    def heapify(self):
        if self.left_child: 
            if self.left_child.left_child: 
              self.left_child.heapify()

            if self.key < self.left_child.key:
                print('-----')
                print("workd")
                temp = self.left_child.key 
                self.left_child.key = self.key 
                self.key = temp 
                self.heapify()
                
            if self.right_child:
                if self.key < self.right_child.key:
                    print("works")
                    temp = self.right_child.key 
                    self.right_child.key = self.key 
                    self.key = temp
                    self.heapify() 
                

        if self.right_child: 
            self.right_child.heapify()

        return self

    def heapify_down(self):
        if self.left_child: 
            if self.left_child.left_child: 
              self.left_child.heapify_down()

            if self.key > self.left_child.key:
                print('-----')
                print("workd")
                temp = self.left_child.key 
                self.left_child.key = self.key 
                self.key = temp 
                self.heapify_down()
                
            if self.right_child:
                if self.key > self.right_child.key:
                    print("works")
                    temp = self.right_child.key 
                    self.right_child.key = self.key 
                    self.key = temp
                    self.heapify_down()  

    def delete_node(self,key): 
        return 

root = heap(4)
list = [10,18,6,2,20]
for i in list: 
    root.insert(i) 

root.pre_order_traversal()
print(root.left_child.left_child.key)
root.heapify()
root.pre_order_traversal()
root.heapify_down()
root.pre_order_traversal()

