def is_anagram(s,t):
    if(len(s)!=len(t)):
        return False
    if sorted(s)==sorted(t):
        return True
    return False

s="triangle"
t='integral'
result=is_anagram(s,t)
print(s ,"and " ,t ," are anagram:",result)