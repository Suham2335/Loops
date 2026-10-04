def password(p):
    while p!=passs:
        print("Incorrect Password.")
        p=input("Enter the password again: ")
    print("login successful")    


p = input("Enter the password: ")
passs="python123"   
password(p) 