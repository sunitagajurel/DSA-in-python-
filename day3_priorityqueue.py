class priorityQueue: 
    def __init__(self,size):
        self.Q= []
        self.size = size

    def isEmpty(self):
        return (len(self.Q)==0)
    
    def isFull(self):
        return (len(self.Q)==self.size)

    def get(self):
        return self.Q.pop(0)

    def put(self,item,priority):
        self.Q.append((priority,item))

    def setPriority(self):
        return self.Q.sort()

pq = priorityQueue(10)
pq.put("rice",2)
pq.put("curry",1)
pq.put("curd",3)
pq.setPriority()
print(pq.get())

    


    