num1=int(input("input enter 1st number:"))
num2=int(input("input enter 2nd number:"))
if num1>num2:
    x=num1
    y=num2
else:
    x=num2
    y=num1
if y==1:
    y=y+1
l1=[]

while (y<x+1):
    for i in range(2,y):
        if (y%i)==0 :
                break
    else:
         l1.append(y)
    y=y+1
print(l1)

