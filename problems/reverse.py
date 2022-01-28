def revereseArray(Arr):
    print(len(Arr))
    for i in range(len(Arr)):
        rev.append(Arr.pop())
        print(rev)
    return rev

rev= []
revereseArray([1,2,3,4,5])
print(rev)
        