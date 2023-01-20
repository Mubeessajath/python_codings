while True:
    try:
        num=int(input("enter the number:"))
        break
    except ValueError:
         print("please input numbers only......")

for i in range(num):
    num=num+i
print("\nanswer is :",num,"\n")
