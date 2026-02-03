import re

str="India,USA,Europe"
dob="16-09-2019"
def dosplit(str,dob):
    regex=r'[,\\s]'
    country_list=re.split(regex,str)
    print(country_list)
    regex_dob=r'[-\\s]'
    dob_list=re.split(regex_dob,dob)
    print(dob_list)

dosplit(str,dob)

    
    
    
    
    