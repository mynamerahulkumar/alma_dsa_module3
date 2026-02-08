def first_non_repeating_char(s):
    for i in range(len(s)):
        is_repeate=False
        for j in range(len(s)):
            if i !=j and s[i]==s[j]:
                is_repeate=True
                break
        if is_repeate==False:
            return s[i]
    return None
s="lovelmario"
first_non=first_non_repeating_char(s)
print(first_non)

# time-O(n*n)
#space-O(n)