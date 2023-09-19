\counter
import time
n=int(input("enter the number"))
while  n:
    print(n)
    n-=1
    time.sleep(1)
else:
    print("counter stop")