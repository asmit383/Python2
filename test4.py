def tinni(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*tinni(x-1)
print(tinni(5))    