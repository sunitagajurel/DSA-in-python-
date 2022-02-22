#Algorithm 
#compares first item of array with second one 
#checks if first < second 
#else swap 
#compare and swap until it compares the second last and last item 

list = [4,5,68,9,0]
def bubblSort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)): 
            if list[i] <list[j]:
                continue 
            else: 
                temp = list[i]
                list[i] = list[j]
                list[j] = temp 
    return list 

print(bubblSort(list))

#since here are two for loops its timecomplexity is 0n**2
#since one extra variable is used space coplexity os 0(1)
