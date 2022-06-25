# Question6. What do you mean by *args and **kwargs?
# Answer--> In cases when we don't know how many arguments will be passed to 
# a function, like when we want to pass a list or a tuple of values, we use *args.

def fun(*args):
    for i in args:
        print(i)
fun(2,64,3,6,7,)        


# **kwargs takes keyword arguments when we don't know how many there will be. 
def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
func(a=1,b=2,c=56)        
