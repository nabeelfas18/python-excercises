def vavels_count():
    print("Enter a String")
    str=input()
    l1=list(str)
    l2=['a','e','o','u']
    flag=0
    for i in l1:
       
        for j in l2:
         if(i==j):
            flag=flag+1

    print(flag)
vavels_count()
