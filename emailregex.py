import re
def emailregex():
    print("Enter The Email")
    str=input()
    email= re.findall("([a-zA-Z0-9_.+-]+@)",str)
    print(email)
    
emailregex()
    