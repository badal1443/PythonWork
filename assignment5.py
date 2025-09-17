# Find smallest number in list
ls = [8,5,1,2,7,3,0,9]
smallest = ls[0]
for i in ls:
    if i < smallest:
        smallest = i
print("Found smallest number as ",smallest)