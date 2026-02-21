def factorial(n):
    #base condition
    if(n==0):
        return 1
    return n*factorial(n-1)

result=factorial(3) #3*2*1*1
print(result)