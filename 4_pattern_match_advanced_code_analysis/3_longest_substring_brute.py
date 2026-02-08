def longest_substring_without_repeating_Character(s):
    longest=''
    len_s=len(s)
    for i in range(len_s):
        substring=''
        for j in range(i,len_s):
            if s[j] in substring:
                break
            else:
                substring+=s[j]
        if(len(substring)>len(longest)):
            longest=substring #abcd
    return longest

s="abcdbccb" # substring=bcd
longest_substring=longest_substring_without_repeating_Character(s)
print(longest_substring)