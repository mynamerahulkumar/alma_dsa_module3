def insertion_sort(arr):
    length=len(arr)
    #[8,6,5,4,7]
    #[8,6]
    
    for i in range(1,length):
        key=arr[i]
        j=i-1
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)
arr=[8,6,5,4,7]
insertion_sort(arr)

        
        