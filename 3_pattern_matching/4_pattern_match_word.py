def wordMatch(word,wordMain):
    len1=len(word)
    len2Main=len(wordMain)
    occurence_index=[]
    #alma #almaxclusivealm
    # range(0,4)
    for i in range(0,len2Main-len1+1):
        k=0
        for j in range(0,len1):
            if(wordMain[i+j]!=word[j]):
                break
            k+=1
        if(k==len1):
            occurence_index.append(i) 
    return occurence_index

wordMain="AlmaxclusivAlma"
word="Alma"
word_occurence_index=wordMatch(word,wordMain)
print(word_occurence_index) 