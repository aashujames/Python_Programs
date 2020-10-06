# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all(4,6,9,4,10,15,2))

# def ens_correct(*greet):
#     if "Colt" in greet and "Steel" in greet:
#         return "welcome back Colt!"
#     return "Not sure who you are"
# print(ens_correct(1, True, "Colt"))
# print(ens_correct('hello', False))


#other than *args
def sum_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all(4,6,9,4,10,15,2))