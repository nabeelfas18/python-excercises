def credentials():
    print("Enter the username")
    name=input()
    print("enter the password")
    password=input()
    print("/////////////")
    print("Re enter your username")
    rename=input()
    if(rename==name):
     print("username confirmed")
    else:
        print("incorect username")
        return 0
    print("Re enter Your password")
    re_password=input()
    if(re_password==password):
     print("passord confirmed")
    else:
        print("incorect password")
        return 0
credentials()
