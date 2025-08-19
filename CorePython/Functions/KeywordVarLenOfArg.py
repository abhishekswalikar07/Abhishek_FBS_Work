def emp(**data):
    for i, j in data.items():
        print(i,":", j)
    print("#######")
    
emp(id=101,name="Pushpa", sal=150,dept="Actor")
emp(name="Abhi",dept="Training",mob="9876543210")
