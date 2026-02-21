def fib(n):
    # base condition or stop condition
    if (n==0):
        return 0
    if (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
result=fib(5)
print(result)