# target value

def does_exist(lst,target):
    for i in lst:
         if i==target:
              return True

    return False 


lst=[3,46,7,6,432,1,13,24,53,22,32]
print(does_exist(lst,66))