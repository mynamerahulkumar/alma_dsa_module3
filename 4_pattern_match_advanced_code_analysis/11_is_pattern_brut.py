def pattern_matching(pattern,s):
    pattern_length=len(pattern)
    str_array=s.split()
    str_length=len(str_array)
    
    #pattern=abc s=""
    #pattern="" s="abde"
    
    #pattern="abbde" s="cat dog dog cat"
    if pattern_length==0 and str_length==0:
        return True
    if pattern_length==0 or str_length==0:
        return True
    if pattern_length!=str_length:
        return False
    
    pattern_map={}
    str_set=set()
    #pattern="abbde" s="cat dog dog cat"
    for i in range(pattern_length):
        char=pattern[i] #a 
        word=str_array[i] #cat
        if char not in pattern_map and word not in str_set:
            pattern_map[char]=word
            str_set.add(word)
        elif pattern_map.get(char)!=word:
            return False
    return True
pattern="abba"
s="cat dog rat cat"
result=pattern_matching(pattern,s)
print(pattern, "and " ,s ," is matched:",result)
        
        
    