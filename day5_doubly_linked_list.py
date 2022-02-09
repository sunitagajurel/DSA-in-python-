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
            new_node.prev = n

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
                n.next.prev = new_node
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
                n.next.prev = new_node
                n.next = new_node


    def forwardTraversal(self):
        n =self.head
        if n is None: 
            print("linked list is empty")
        else: 
            while n is not None:
                print(n.data ,'--> ', end = " ")
                n= n.next 

    def reverseTraversal(self):
        print("reverse traversal")
        if self.head is None: 
            print("Linked list is empty")
        else: 
            n = self.head
            while n.next is not None:
                n = n.next
                
            while n is not None: 
                print(n.data,'---->',end = " ")
                n = n.prev

        # print(self.head.next.next.data)
    def removeAtBegin(self):
        if self.head is None: 
            return "linked list is empty"
        else: 
            self.head = self.head.next
            self.head.prev = None

    def removeAtValue(self,value):
        if self.head is None: 
            return "linked list is empty"

        if self.head.data is value : 
            print("first data ")
            self.head = self.head.next
            self.head.prev = None
            return 

        else : 
            n = self.head
            while n.next is not None: 
                if n.next.data is value:
                    print(n.next.data)
                    break 
                n = n.next

            if n.next is None: 
                print("No data found")
                return 

            if n.next.next is None: 
                n.next = None
                return 
            
            else : 
                n.next = n.next.next
                n.next.prev = n


    
    def removeAtEnd(self):
        if self.head is None: 
            return "linked list is empty"

        if self.head.next is None : 
            self.head = self.head.next
            self.head.prev = None
            return 

        n = self.head
        while n.next.next is not None:
            n = n.next 
        n.next = None

db = doublyLinkedList()
db.insertAtBegin(10)
db.insertAtBegin(100)
db.insertAtBegin(50)
db.insertAtEnd(20)
db.insertBeforeValue(40,10)
db.insertAfterValue(60,40)
db.forwardTraversal()
db.removeAtBegin()
db.forwardTraversal()
db.removeAtEnd()
db.forwardTraversal()
db.removeAtValue(10)
db.reverseTraversal()




