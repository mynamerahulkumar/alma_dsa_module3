# Ternary operator
a=10
b=20
max_value=a if a>b else b
print(max_value)

#check for specific values

number=6
if number==5:
    print("number equals 5")
else:
    print("number not equals 5")
    
#while loop print 1 to 100
i=1
print("while loop started---")
while(i<=100):
    print(i)
    i=i+1

#writes 2's table with the help of while loop
# print("2s table")
a=2 
i=1
while(i<=10):
    t=a*i
    print(a,"*",i,"=",t)
    i=i+1

# print("2s table completed")

#while loop infinite
print("while loop infinite started")
while True:
    response=input("Do you want to continue?(Yes/No)")
    if response.lower()=="no":
        break # exit the while loop
    print("Continue the loop")

print("Loop has been terminated")

#For loop

#for loop with condition print 1 to 5
print("For loop started---")
for number in range(1,6):
    print(number)
    
#For loop with this list
fruits=["orange","apple","guava"]
for fruit in fruits:
    print(fruit)

# word="alma"

for letter in word:
    print(letter)

# for loop print 1,20 but with gap 2 (1,3,5,7)
# i=1
while(i<=20):
    print(i)
    i=i+2

for i in range(1,20,2):
    print(i)

#For loop with the continue and break 
print("for with the continue--")
for i in range(1,6):
    if i==3:
        continue #skip the current iterations when i is 3
    print(i)

print("for with the break--")
for i in range(1,6):
    if i==3:
        break
    print(i)

print("for loop break")
    





