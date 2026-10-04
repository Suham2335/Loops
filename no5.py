def dupli():
    str = input("Enter a string: ")

    for i in range(0,len(str)):
        for j in range(i + 1,len(str)):
            if str[i]==str[j]:
                print(f"First character that repeats more than once is {str[i]}")
                exit()
            

dupli()