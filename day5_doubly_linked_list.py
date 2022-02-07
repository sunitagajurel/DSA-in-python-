from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class doublyLinkedList: 
    def __init__ (self) :
        self.head = None

    def insertAtBegin(self,data): 
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            return 
        else:
            print("first node already exist")
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
        else: 
            n = self.head
            while n.next is not None: 
                n = n.next
            n.next = new_node
            new_node.prev = self.head

        

    def insertBeforeValue(self,data,value):
        if self.head is None: 
            return "linked list is empty"
        new_node = Node(data)

        if self.head.data is value: 
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node

        else :
            n= self.head
            while n.next is not None: 
                if n.next.data  is value: 
                    break 
                n = n.next 
            if n.next is None: 
                return "no value found" 
            else: 
                new_node.prev = n 
                new_node.next = n.next 
                n.next = new_node

    def insertAfterValue(self,data,value):
        if self.head is None: 
            return "linked list is empty"
        else:
            new_node = Node(data)
            n= self.head
            while n.next is not None: 
                if n.data  is value: 
                    break 
                n = n.next 
            if n.next is None: 
                return "no value found" 
            else: 
                new_node.prev = n 
                new_node.next = n.next 
                n.next = new_node

    def forwardTraversal(self):
        if self.head is None: 
            print("linked list is empty")
        else: 
            while self.head is not None:
                print(self.head.data ,'--> ', end = " ")
                self.head = self.head.next

        # print(self.head.next.next.data)
        

    def reverseTraversal():
        return 
    
    def removeAtBegin():
        return 

    def removeAtValue():
        return 
    
    def removeAtEnd():
        return 


db = doublyLinkedList()
db.insertAtBegin(10)
db.insertAtBegin(100)
db.insertAtBegin(50)
db.insertAtEnd(20)
db.insertBeforeValue(40,10)
db.insertAfterValue(50,40)
db.forwardTraversal()



