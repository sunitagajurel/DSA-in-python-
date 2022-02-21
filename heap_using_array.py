class heap: 
    def __init__(self,capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size =0
#[1,2,5,10,15,20]
    def getParentIndex(self,index):
        return (index-1)//2

    def hasParent(self,index):
        if self.getParentIndex(index)>=0: 
            return True
    
    def getLeftChildIndex(self,index):
        return ((index*2) +1)

    def hasLeftChild(self,index):
        if self.getLeftChildIndex(index)< self.size:
            return True

    def getRightChildIndex(self,index):
        return ((index*2)+2)

    def hasRightChild(self,index):
        if self.getRightChildIndex(index) < self.size:
            return True

    def isFull(self): 
        if self.size == self.capacity:
            return True

    def parent(self,index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]


    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insertData(self,data): 
        if self.isFull(): 
            raise"the capcity is full" 
        self.storage[self.size]= data
        self.size += 1 
        self.heapifyUp(self.size -1)

    def heapifyUp(self,index): 
        if self.hasParent(index) and self.parent(index) > self.storage[index]: 
            self.swap(self.getParentIndex(index),index)
        if self.hasParent(index): 
            self.heapifyUp(self.getParentIndex(index))
        return

    def removeMin(self):
        if(self.size == 0):
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0]= self.storage[self.size-1]
        self.size -=1 
        index = 0
        self.heapifyDown(index)
        return data 

    def heapifyDown(self,index): 
        if self.hasLeftChild(index): 
            smallChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) <self.leftChild(index)): 
                smallChildIndex = self.getRightChildIndex(index)
            if (self.storage[index] <self.storage[smallChildIndex]):
                return  
            else: 
                self.swap(index,smallChildIndex)
            self.heapifyDown(smallChildIndex)
        
root = heap(10)
root.insertData(20)
root.insertData(10)
root.insertData(25)
root.insertData(50)
print(root.storage)
print(root.removeMin())
