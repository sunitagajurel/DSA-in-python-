list = [0,10,8,50,1,-8]

def mergeSort(list): 
    #split the list until the list contain single element 
    if len(list) >1:  #base case 
        half  = len(list)//2
        left_list = list[:half]
        right_list= list[half:]
        mergeSort(left_list)
        mergeSort(right_list)

        i= j =k = 0 

        #merge the left and rigt list 
        while i < len(left_list) and j < len(right_list) :
            if left_list[i] < right_list[j]: 
                list[k] = left_list[i]
                i += 1
            else: 
                list[k] = right_list[j]
                j += 1
            k += 1 

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1 
            k += 1 

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

mergeSort(list)
print(list)

