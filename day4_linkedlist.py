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

    def insertAtEnd(self,data):
        new_node= Node(data)
        if self.head is None:
           self.head = new_node
        else: 
            n = self.head
            while n.Next is not None: 
                n = n.Next
            n.Next = new_node

    def insertAtMid(self,pos,data): 
        new_node = Node(data)
        n = self.head
        while n.data is not pos:
           n =n.Next
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


lL= LinkedList()
lL.insertAtBegin(20)
lL.insertAtBegin(50)
lL.insertAtEnd(60)
lL.insertAtMid(50,80)
print(lL.traversal())




