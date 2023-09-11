

''' all the divisors of the given number'''
n=int(input("enter the number of which u want divisors"))
count=0
sum=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count=count+1
        sum=sum+i
print("number of divisors",count)
print("sum of numbers:",sum)
    