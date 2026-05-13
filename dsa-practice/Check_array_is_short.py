nums = [1,2,3,8,6,7,10]
n = len(nums)

is_sorted = True
for i in range(0,n - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
      
print(is_sorted)