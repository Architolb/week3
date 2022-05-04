from statistics import mean
from random import randint

nums = [randint(0, 100) for x in range(20)]
for i in nums:
    if i in nums > mean(nums):
        print

mean(nums) 
print(mean(nums))
