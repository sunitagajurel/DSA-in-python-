class Queue: 
    #initialize queue attributes
    def __init__(self,capacity): 
        self.front = self.rear = -1 
        self.size = 0
        self.Q=[]
        self.capacity = capacity

    #check if queue is full
    def checkFull(self):
        return self.size == self.capacity

    #Check if queue is empty
    def checkEmpty(self):
        return self.size == 0

    #insert items in the queue
    def EnQueue(self,item):
        if self.checkFull(): 
            return"queue is full"

        self.rear= self.rear+1
        self.Q.append(item)
        self.size = self.size + 1
        return ("{} is inserted into the queue".format(item))
    
    #remove items from the queue 
    def DeQueue (self): 
        if self.checkEmpty():
            return "stack is empty"
        self.front = self.front +1
        self.Q.pop(0)
        print("{} dequeued from the queue".format(self.Q[self.front]))
        self.size = self.size-1
        self.rear= self.rear-1

    def que_front(self):
        if self.checkEmpty():
            print("Queue is empty")
 
        print("Front item is", self.Q[self.front])
         
    # Function to get rear of queue
    def que_rear(self):
        if self.checkEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])
    
queue = Queue(20)
queue.EnQueue(5)
queue.EnQueue(5)
queue.EnQueue(60)
queue.DeQueue()
queue.que_front()
queue.que_rear()

        
    