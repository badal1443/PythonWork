## Find smallest and largest number entered by user

smallest = None
largest = None
count=0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if smallest is None and largest is None:
            smallest=num
            largest=num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    except:
        print("Invalid input")
        continue
    count = count + 1
print("Maximum is",largest)
print("Minimum is",smallest)