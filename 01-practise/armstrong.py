n=153
num=n
totallen=len(str(n))
sum=0
while num>0:
    last_digit=num%10
    sum= sum+(last_digit**totallen)
    
    num=num//10   

print(sum==n)
# time compnxcity O(log10(N))
# space complixicy O(1)