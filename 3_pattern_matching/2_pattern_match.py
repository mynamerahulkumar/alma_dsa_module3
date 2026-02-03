import re 

## 11-30-2025

regex_dob=r'\d{2}-\d{2}-\d{4}'
word='India'
replace_word=r'my'

def checksentence(sentence):
    is_dob=re.search(regex_dob,sentence)
    
    word_regex=re.compile(word)
    
    
    is_word=word_regex.search(sentence)
    
    new_sentence=re.sub(replace_word,"our",sentence)
    
    if(is_dob!=None):
        print("DOB is present")
    else:
        print("dob is not present")
    if(is_word!=None):
        print(word,"is present")
    else:
        print(word,"is not present")
    print(new_sentence)

sentence="India is my country.My DOB 31-01-2019"

checksentence(sentence)

