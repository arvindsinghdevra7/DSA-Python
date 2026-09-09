marks = {
    'math':33,
    'physics':45,
     'bio':33,
}

totaln= len(marks)
total = sum(marks.values())

print(f"average:{total/totaln}")