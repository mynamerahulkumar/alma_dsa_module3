#Custom functions

def mul(a,b):
    p=a*b #p=2*3=6
    return p

p=mul(2,3)
print(p)

#count the occurence of each unique letter in a given word and returns a dictionary

# papaya {"p":2,"a":3,"y":1}

# print("unique letter function")
#papaya
#{"p":2,"a":3,"y":1}
def count_letter(word):
    letter_count={}
    for letter in word:
        letter=letter.lower()
        letter_count[letter]=letter_count.get(letter,0)+1 #
    return letter_count

d=count_letter("Papaya")
print(d)

# reverse the string 

string_input="hello world"

def reverse_string(str1):
    reverse_string=str1[::-1]
    return reverse_string

s=reverse_string(string_input)
print(s)


def calculate_calories_burner(duration_mins,activity):
    calories_burned=0 #8,16,24
    #duration_mins=10,9,8,7.   0
    while(duration_mins>0):
        if activity.lower()=="runing":
            calories_burned+=10
        elif activity.lower()=="swimming":
            calories_burned+=8
        elif activity.lower()=="cycling":
            calories_burned+=6
        duration_mins-=1
    print("activity completed and caloried burned=",calories_burned)

calculate_calories_burner(10,"swimming")

#lambda arg expression
print("lambda functions----")
add= lambda x,y:x+y
result=add(5,10)
print(result)

mul= lambda x,y:x*y
result=mul(5,10)
print(result)

# lambda with filters

print("lambda with filters--")
numbers=[1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if(num%2==0):
        print(num)
        
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)