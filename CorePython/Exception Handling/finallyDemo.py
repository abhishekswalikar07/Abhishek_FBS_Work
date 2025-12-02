def division(x,y):
    try:
        div=x/y
    except ZeroDivisionError as e:
        print(f'Error:{e}')
    except Exception as e:
        print(f'Error:{e}')
    else:
        print(div)
    finally:
        return f'Program executed successfully...'
    
x=int(input("Enter dividend:"))
y=int(input("Enter divisor:"))
print(division(x,y))