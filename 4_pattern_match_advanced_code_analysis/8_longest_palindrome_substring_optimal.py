
def expand_around_center(s,left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left=left-1
        right=right+1
    return s[left+1:right]
# aba left=1,right=1 ,left=0,right=2,left=-1,right=3
#s[0:3]=b

def longest_palindrome_substring(s):
    longest=""
    for i in range(len(s)):
        odd_palindrome=expand_around_center(s,i,i)
        even_palindrom=expand_around_center(s,i,i+1)
        current_longest=""
        if(len(odd_palindrome)>len(even_palindrom)):
            current_longest=odd_palindrome
        else:
            current_longest=even_palindrom
        if(len(current_longest)>len(longest)):
            longest=current_longest
    return longest

s="babacd"
longest_pal=longest_palindrome_substring(s)
print(longest_pal)
