def oddlist():
    l1=[1,2,3,4,5,6,7,'A']
    l2=[]
    for i in range(len(l1)):
        if(i%2!=0):
            l2.append(l1[i])

    print(l2)
oddlist()
         
