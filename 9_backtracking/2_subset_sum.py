solution=[]
def find_subset_sum(arr,target,start,current_sum):
    
     if(current_sum==target):
         print(solution)
         return
     # try all possible combination
     if(current_sum>target):
         return
     for  i in range(start,len(arr)):
         solution.append(arr[start])
         find_subset_sum(i+1,current_sum+arr[i])
         solution.pop()
arr=[1,2,3,4,5]
target=7
start=0
current_sum=0
find_subset_sum(arr,target,start,current_sum)
        
            