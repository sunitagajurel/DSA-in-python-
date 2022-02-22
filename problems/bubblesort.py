#Algorithm 
#compares first item of array with second one 
#checks if first < second 
#else swap 
#compare and swap until it compares the second last and last item 

array = [4,5,68,9,0]
list = [0,1,2,3,4]

def bubblSort(list):
    bcount = 0
    for i in range(len(list)):
        for j in range(len(list)-i-1): 
            bcount += 1 
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp 
    print(bcount)
    return list 

#this optimized algorithm checks if the array is already sorted 
def optimizedBubbleSort(list):
    ocount = 0
    for i in range(len(list)):
        swapped = False 
        for j in range(len(list)-i-1): 
            ocount += 1 
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp 
                swapped = True
                print(list)
            
        if not swapped: 
            break
    print(ocount)

    return list 


print(bubblSort(list))
print(optimizedBubbleSort(array))


# #since here are two for loops its timecomplexity is 0n**2
# #since one extra variable is used space coplexity os 0(1)






    