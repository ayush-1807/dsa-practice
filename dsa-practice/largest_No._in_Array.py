# nums =[8,5,11,20,24]
nums = list(map(int, input().split()))
n = len(nums)
largest = nums[0]
for i in range(0,n):
    if nums[i] > largest:
        largest = nums[i]
print(largest)
    
    


