from sympy import N


class Node: 
    #each node contains data and link of the next node
    def __init__(self,data):
        self.data = data 
        self.Next = None
class LinkedList: 
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.Next = self.head
        self.head = new_node

    def insert(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
        else: 
            print("no position defined")


    

    def insertAtEnd(self,data):
        new_node= Node(data)
        if self.head is None:
           self.head = new_node
        else: 
            n = self.head
            while n.Next is not None: 
                n = n.Next
            n.Next = new_node

    def insertAfter(self,pos,data): 
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == pos:
               break
            n = n.Next
        if n is None:
            print("no such node found")
        else: 
            new_node.Next = n.Next
            n.Next= new_node
    
    def insertBefore(self,pos,data):
        if self.head is None: 
            print("Linked list is empty")
            return 
        
        if self.head.data == pos: 
            self.insertAtBegin(data)
            return

        new_node = Node(data)
        n = self.head
        while n.Next is not None: 
            if n.Next.data == pos:
                break
            n =n.Next        
        if n.Next is None:
            print("no such node found")
        else: 
            new_node.Next = n.Next
            n.Next= new_node

    def traversal (self): 
        if self.head is None: 
            return "Linked List is empty"
        else:
            n = self.head
            while n is not None: 
                print(n.data,"---->",end = " ") #self.head.data, self.head.Next.data,self.head.Next.Next.data
                n = n.Next

    def deleteAtBegin (self):
        if self.head is None: 
            print("List is empty")
            return  
        self.head = self.head.Next

    def deleteAtEnd (self):
        if self.head is None: 
            print("List is empty")
            return 
        
        elif self.head.Next is None: 
            self.head = None

        else: 
            n= self.head
            while n.Next.Next is not None: 
                n= n.Next 
            n.Next = None
            return
    
    def deleteAtMid(self,pos):
        if self.head is None: 
            print("List is empty")
            return 

        if self.head.data is pos : 
            self.head = self.head.Next
            return 

        n= self.head
        while n.Next is not None:
            if n.Next.data == pos:
                break 
            n = n.Next
                
        if n.Next is None: 
            print("no such node found")
            return 
        else: 
            n.Next = n.Next.Next

lL= LinkedList()
lL.insert(20)
lL.insertAtBegin(50)
lL.insertAtEnd(60)
lL.insertAfter(20,10)
lL.insertBefore(10,80)
lL.deleteAtMid(500)
print(lL.traversal())






