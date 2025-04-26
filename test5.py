def asmit(*args):
    print(args)
    return sum(args)
print(asmit(1,3,4,5))

def abhi(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}={value}")
abhi(name="Asmit",age=20,country="India")        