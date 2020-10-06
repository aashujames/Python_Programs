nums = [1,2,3]
y = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            y+=1
        else:
            y+=0
        
print(f"good pairs = {y}")