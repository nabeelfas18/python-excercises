def map_list():
    print("Enter the first list")
    l1=input()
    firstlist=l1.split()
    d={}
    print("Enter the second list")
    l2=input()
    secondlist=l2.split()

    for i in firstlist:
        for j in secondlist:

         d.update({i:j})
    print(d)
map_list()