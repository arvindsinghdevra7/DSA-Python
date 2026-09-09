def find_max(a,b,c):
    if a>b and a>c:
        print(a,'is maximum')
    elif b>a and b>c:
        print(b,'is maximum')
    else:
        print(c,'is maximum')

a=int(input('Enter a number a :'))
b=int(input('Enter a number b :'))
c=int(input('Enter a number c :'))

find_max(a,b,c)