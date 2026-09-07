start = int(input('Enter a number: '))
end = int(input('Enter a number: '))

i=start
while i<=end:
    if i%3==0 and i%5==0:
        print(i)
    i+=1
