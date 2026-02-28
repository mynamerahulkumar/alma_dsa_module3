def find_all_combination(arr,index,current):
    #base condition
    length_of_array=len(arr)
    if(index==length_of_array):
        print(current)
        return
    #Choice 1-Exclude the current element
    find_all_combination(arr,index+1,current)
    #Choice 2-Include the current Element
    find_all_combination(arr,index+1,current+[arr[index]])

arr=['a','b','c']
find_all_combination(arr,0,[])