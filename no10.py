import time
def cdown():
    n = int(input("Enter a number to start countdown: "))
    while n>=0:
        print(n)
        n=n-1
        time.sleep(1)

cdown()