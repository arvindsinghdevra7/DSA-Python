start = int(input('Enter a number: '))
end = int(input('Enter a number: '))
sum=0
i=start

while i<=end:
    if i%2==0 and i%7==0:
       print(i,end=' ')
       sum=sum+i
    i=i+1
print(sum)    
