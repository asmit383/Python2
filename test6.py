def asmit(char):
    x=[]
    
    for i in char:
        if i not in x:
            count=char.count(i)
            x.append(i)
            print(i,"=",count)
asmit("Diposree")            