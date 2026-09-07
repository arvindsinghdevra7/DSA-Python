# n = 20
# result = []
# for i in range(1,n+1):
#     if n%i==0:
#        result.append(i)
# print(result)

n=10
result=[]
for i in range(1,n//2):
    if n%i==0:
       result.append(i)
result.append(n)
print(result)       