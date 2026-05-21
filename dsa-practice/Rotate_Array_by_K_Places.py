nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):

    n = len(nums)

    k = k % n

    for _ in range(k):

        e = nums.pop()

        nums.insert(0, e)

    return nums

print(rotate(nums, k))