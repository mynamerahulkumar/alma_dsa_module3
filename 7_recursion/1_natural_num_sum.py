def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

result=sum(3)
print(result)