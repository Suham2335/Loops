def evenodd(n):
    Result=""
    if n%2==0:
        Result="Even"
    else:
        Result="Odd"
    return Result

n = int(input("Enter a number: "))  
print(f"Given number is {evenodd(n)}")  
