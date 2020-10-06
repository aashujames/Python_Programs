# nums = list(range(1,5))
# print(f"nums = {nums}")
# arr= []
# arr.append(nums[0])
# for v in range(1,len(nums)):
#     arr.append(arr[v-1]+nums[v])
# print(f"arr = {arr}")

#modified of above
nums = list(range(1,5))
print(f"nums = {nums}")
for i in range(1,len(nums)):
    nums[i] += nums[i-1]   #nums[i] = nums[i]+nums[i-1n]
print (f"new nums = {nums}")