list = [7,8,0,50,-5]
def selectionSort(list): 
    scount = 0
    for i in range(len(list)): 
        min = list[i]
        for j in range(i+1, len(list)): 
            print(list[j],min)
            scount += 1
            if list[j] < min:
                min = list[j] 
                list[j] = list[i]
                list[i] = min 
    print(scount)
    return list

print(selectionSort(list))