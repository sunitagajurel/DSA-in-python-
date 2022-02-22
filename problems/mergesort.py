def mergeSort(array): 
    if len(array) > 1: 
        h = len(array)//2
        l = array[:h]
        r = array[h:]
        print(l)
        print(r)
        mergeSort(l)
        mergeSort(r)

        i= j = k =0

        #until we reach end of left and right sub-arrays  
        while i < len(l) and j < len(r):
            print("i is",i)
            print("left is ",l)
            print("right is",r)
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1
        print ("array is ",array)
        print("length of l", len(l))

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        print ("array after sorting is ",array)

       
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
        print ("array after sorting is ",array)
        

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1,50,0]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)