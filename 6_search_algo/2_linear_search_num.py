def linear_search(arr,target):
    
    for index in range(len(arr)):
        if(arr[index]==target):
            return arr[index]
    return -1

arr=[34,56,78,97,35,21,21,9,24]
target=100
result=linear_search(arr,target)
if(result==-1):
    print(target," is not present in ",arr)
else:
    print(target, " is present")
#time -O(n)
#space -O(1)