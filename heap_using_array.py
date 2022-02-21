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

    def righChild(self,index):
        return self.storage[self.getRightChildIndex(index)]


    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    # def insertData(self,data): 
    #     if self.isFull(): 
    #         return"the capcity is full" 
    #     self.storage[self.size]= data
    #     self.size += 1 
    #     self.heapifDown()

    # def heapifyDown(self):
    #     index = self.size -1 
    #     while self.hasParent(index) and self.leftChild(index) > self.storage[index]: 
    #         self.swap(index)
        


root = heap(10)
root.insert(15)
root.insert(10)
print(root.storage)
