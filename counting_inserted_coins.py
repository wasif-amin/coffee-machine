uarter= 0.25
dime= 0.10
nickle= 0.05
penny= 0.01
def money():
    print("insert coins")
    num_quarters = int(input("quarters: ")) * quarter
    num_dimes = int(input("dimes: ")) * float(dime)
    num_nickles= int(input("nickles: ")) * float(nickle)
    num_pennies = int(input("pennies: ")) * float(penny)
    total = num_quarters + num_dimes + num_nickles + num_pennies
    return total
change = money()
print(change)
