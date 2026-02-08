def is_palindrom(s):
    s1=s
    s2=s[::-1]
    if(s1==s2):
        return True
    else:
        return False
# reverse Time-O(n)
def longest_palindrome_substring(s):
    longest=''
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]
            # time-(O(n*n))
            if is_palindrom(substring) and len(substring)>len(longest):
                longest=substring
             # time-(O(n*n*n))
                
    return longest

s="babacd"
longest_pal=longest_palindrome_substring(s)
print(longest_pal)
 # time-(O(n*n*n))
 # space -(n)