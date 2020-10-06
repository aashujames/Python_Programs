# nums = [2,5,1,3,4,7]
# arr=[]
# x=[]
# y=[]
# for i in range((len(nums))//2):
#     x.append(nums[i])
# for j in range((len(nums))//2,len(nums)):
#     y.append(nums[j])
# for k in range(len(nums)//2):
#     arr.extend([x[k],y[k]])
# print(f"arr = {arr}")


# nums = [2,5,1,3,4,7]
# arr=[]
# x=[]
# y=[]
# for i in range(0,len(nums)):
#     if i<len(nums)/2:
#         x.append(nums[i])
#     else:
#         y.append(nums[i])
# for k in range(len(nums)//2):
#     arr.extend([x[k],y[k]])
# print(f"arr = {arr}")


#short and fast method
nums = [1,2,3,4,4,3,2,1]
arr = []
n = len(nums)//2
for i in range(n):
    arr.extend([nums[i],nums[i+n]])
print(arr)



