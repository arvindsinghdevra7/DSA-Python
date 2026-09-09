def calcul(nums):
    n = len(nums)
    total=0
    for num in nums:
        total= total+num
    return total/n

nums=[23,54,423,445,24,2,32]

print(calcul(nums))

