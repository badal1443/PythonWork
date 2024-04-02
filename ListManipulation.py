## Working with list with few tricks.

data = ["John","Doe","875634345","some street","98656","45"]
fname,lname,*_,age=data
print(f"{fname} {lname} is {age} years old.")


## Find max occurance from following array.
arr=[1,2,4,3,2,5,1,3,5,1,2,1]
m= max(arr,key=arr.count)
print(m)
## but we need to know which number occured most of the time.

