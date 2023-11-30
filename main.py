def summa(a,b):
    return a+b
print(summa(100000000000000000000000,1000000000000000000000000000000000000000000000000000000000000000))





def dec(func):
    def wrapper(a):
        print("----------------------------")
        return a ** 2
    return wrapper
@dec
def func(a):
    return a


print(func(1000000000000000000000000000000000000000))