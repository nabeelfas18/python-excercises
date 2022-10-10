def count():
    print("enter the list items")
    items=input()
    l=items.split()
    flag=0
    dict1={}
    for i in l:
        for j in l:
            if(i==j):
                flag=flag+1
                dict1.update({i:flag})
        flag=0
    print(dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True)))
count()