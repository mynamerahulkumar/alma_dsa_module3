def remove_duplicates(arr):
    dict1=dict.fromkeys(arr)
    uniqueList=list(dict1)
    print(uniqueList)

arr=[20,25,20,30,40]
remove_duplicates(arr)