def evenOdd():  # Function defination
    # Function Body
    num=int(input("Enter number to check even or odd:"))
    if num==0:
        print("Number is zero")
    elif num%2==0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')
        
evenOdd() # Function call