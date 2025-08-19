def power(m, n):
    
    if n == 0:
        return 1
     
    return m * power(m, n - 1)

m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))
print(f"{m}^{n} = {power(m, n)}")
