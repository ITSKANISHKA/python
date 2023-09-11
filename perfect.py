""" perfect number or non perfect numbers"""
n=int(input("enter a nmber"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=i
if i==n:
    print("its a perfect number")
else:
    print("its not a perfect number")