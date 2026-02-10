def is_anagram(s,t):
    if(len(s)!=len(t)):
        return False
    char_count={}
    for char in s:
        char_count[char]=char_count.get(char,0)+1
    
    for char in t:
        if char not in char_count or char_count[char]==0:
            return False
        char_count[char]-=1
    return True
s="triangle"
t="integral"
result=is_anagram(s,t)
print(s," and ",t," are anagram: ",result)

# time ~O(n)
# space-O(n)