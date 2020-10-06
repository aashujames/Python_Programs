# def add_n_multi(a,b,c):
#     print(a+b*c)
# data = dict(a=1,b=2,c=3)
# add_n_multi(**data)

# some modifications of above
def add_n_multi(a,b,c,**kwargs):
    print(a+b*c)
    print("Other stuff...")
    print(kwargs)
data = dict(a=1,b=2,c=3,d=55,name="Bosh")
add_n_multi(**data, dog='black')


