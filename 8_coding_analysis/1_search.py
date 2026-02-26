def findElememt(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            return mid 
        elif(arr[mid]>target):
            right=mid-1
        elif(arr[mid]<target):
            left=mid+1
    return -1
arr=[10,15,20,25,30]
target=25
resultIndex=findElememt(arr,target)
print(resultIndex)