def longest_substring_without_repeating_Character(s):
    longest=''
    start=0
    char_map={}
    for end in range(len(s)):
        if s[end] in char_map:
            start=max(start,char_map[s[end]]+1)
        char_map[s[end]]=end
        sub_string=s[start:end+1]
        if(len(sub_string)>len(longest)):
            longest=sub_string
    return longest
  
s="abcdbccb" # substring=bcd
longest_substring=longest_substring_without_repeating_Character(s)
print(longest_substring)