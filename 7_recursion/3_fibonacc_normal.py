def fib(n):
    firstNum=0
    secondNum=1
    print(firstNum)
    print(secondNum)
    for i in range(1,n+1):
        nextNum=firstNum+secondNum
        print(nextNum)
        firstNum=secondNum
        secondNum=nextNum

fib(4)
# 0 1 1 2 3 5