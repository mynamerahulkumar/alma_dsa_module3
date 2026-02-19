def two_sum(arr,target):
    num_map={}
    for i in range(len(arr)):
        complement=target-arr[i] #11-9=2, #2+9=11
        if complement in num_map:
            print("sum of ",arr[i]," and ",complement ,"is equals to ",target)
        num_map[arr[i]]=i
    return -1
arr=[4,2,19,9]
target=11
result=two_sum(arr,target)
# time-O(n)
# space-O(n)