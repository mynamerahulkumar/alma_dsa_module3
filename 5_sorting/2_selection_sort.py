def selectionSort(arr):
    length=len(arr)
    #[5,4,3,2,9,8]
    #[0,1,2,3,4,5]
    #min_index=0
    #[2,4,3,5,9,8]
    #[2,3,4,5,9,8]
    for i in range(length):
        min_index=i
        for j in range(i+1,length):
            if(arr[j]<arr[min_index]):
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
    print(arr)
    
arr=[5,4,3,2,9,8]
selectionSort(arr)
        