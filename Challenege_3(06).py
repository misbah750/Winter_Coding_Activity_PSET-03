def repeatedNTimes(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
# Test cases
print(repeatedNTimes([2,1,2,5,3,2]))
print(repeatedNTimes([9,5,3,9]))
print(repeatedNTimes([7,8,7,7]))