hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r= float(rate)

extra_hours = h - 40
total=0

if extra_hours <=0:
    total= h * r
else:
    total = ((h-extra_hours)*r)+(extra_hours*r*1.5)
print(total)