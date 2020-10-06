# from random import random
# def flip_coin():
#     r = random()
#     if r>0.5:
#         print("head")
#     else:
#         print("tail")
# flip_coin()


from random import random
def flip_coin():
    r = random()
    if r>0.5:
        return "head"
    else:
        return "tail"
print(flip_coin())