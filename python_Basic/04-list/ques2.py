# largest num

nums=[23,46,7,42,2,5,7,4,23,1]
max = float('-inf')

for num in nums:
    if num>max:
        max=num

print(max)        