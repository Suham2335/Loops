def neg_count(numbers):
   

    count=0

    for number in numbers:
        if number<0:
            count+=1

    return count        

numbers = [2,-3,4,-5,-6,7,8,-9]

print(f"Count of Negative Numbers is {neg_count(numbers)}")            

    
