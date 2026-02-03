def reverseArray(arr):
    start=0
    end=len(arr)
    while(start<end): #0<5
        temp=arr[start]
        arr[start]=arr[end-1]
        arr[end-1]=temp #[45,34,235,56,1]
        start+=1
        end-=1
    print(arr)
    
arr=[1,34,235,56,45]
reverseArray(arr)

# time O(n/2)~ o(n)
# space o(1)