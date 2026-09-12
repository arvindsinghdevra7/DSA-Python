import copy
original=[1,2,3,[1,3,4]]
shallow=copy.deepcopy(original)

print(id(original))
print(id(shallow))
shallow[3][1]=233

print(shallow)
print(original)