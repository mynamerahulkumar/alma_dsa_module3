def find_second_smallest(array):
    smallest=float('inf') #2,1,0
    second_smallest=float('inf') #inf 5 ,2,1
    
    for num in array:
        if num<smallest:
            second_smallest=smallest #inf,
            smallest=num #2
        elif smallest<num <second_smallest:
            second_smallest=num
    if(second_smallest==float('inf')):
        print("there is no second smallest element")
        return
    print("second smallest element=",second_smallest)
    print("smallest element=",smallest)
array=[2,5,10,1,0]
find_second_smallest(array)

# time -O(n)
#space-o(1)
            