# def fav_color(**kwargs):
#     print(kwargs)
# fav_color(colt='purple', ashish='red', aditya='blue')

#other than kwargs
# def fav_color(**intro):
#     print(intro)
# fav_color(colt='purple', ashish='red', aditya='blue')

def special_greet(**kwargs):
    if 'David' in kwargs and kwargs['David'] == 'special':
        return "You get a special greeting David."
    elif 'David' in kwargs:
        return f"{kwargs['David']} David."
    return "Not sure who this is.."
print(special_greet(David='Hello'))
print(special_greet(Bob='hello'))
print(special_greet(David='special'))
print(special_greet(Heather='lol', David='special'))