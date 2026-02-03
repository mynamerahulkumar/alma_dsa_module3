import re
def validateEmail(email):
    #regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    email_regex=r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    is_valid_email=re.match(email_regex,email)
    return is_valid_email

email1="raj@gmail.com"
email2="alma.gmail.com"

email_list=[email1,email2]

for email in email_list:
    result=validateEmail(email)
    if(result!=None):
        print(email,"is valid email")
    
    else:
        print(email,"is not valid email")



    