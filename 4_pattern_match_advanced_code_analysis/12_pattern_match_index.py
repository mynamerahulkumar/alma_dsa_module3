def pattern_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    occurences=[]
    for i in range(n-m+1):
        j=0
        while(j<m):
            if(text[i+j]!=pattern[j]):
                break
            else:
                j+=1
        if j==m:
            occurences.append(i)
            i=i+m-1
       
    return occurences

text="abaabacabad"
pattern="aba"
result=pattern_matching(text,pattern)
print(pattern,"and " ,result,"matching indexes:",result)

# Time -O(n*m)
# space-O(k) matching times=k