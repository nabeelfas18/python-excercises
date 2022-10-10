def searchdict():
    rollno=[44,64,69,37,76,83,95,97]
    roll=rollno.copy()
    sampledict={'sojo':44,'thomas':69,'tom':76,'jack':11}
    valuelist=list(sampledict.values())
    
    for i in roll:
        flag=0
        for j in valuelist:
            if(i==j):
                flag=1
                break
        if flag==0:
            rollno.remove(i)    
            
        
    print(rollno)
searchdict()
