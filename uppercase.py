def count(str):
    lower=0
    upper=0
    for i in str:
        if(i.islower()):
            lower+=1
        else:
            upper+=1

    print("The number of lowercase characters is:",lower)
    print("The number of uppercase characters is:",upper)
print("Enter a string")
str=input()
count(str)