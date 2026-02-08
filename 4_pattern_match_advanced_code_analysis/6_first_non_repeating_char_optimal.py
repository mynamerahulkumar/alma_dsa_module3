def first_non_repeating_char(s):
   char_count={}
   for char in s:
       char_count[char]=char_count.get(char,0)+1
   for char in s:
        if char_count[char]==1:
            return char
   return None
s="lovelmario"
first_non=first_non_repeating_char(s)
print(first_non)

# time-O(2n)~O(n)
#space-O(n)