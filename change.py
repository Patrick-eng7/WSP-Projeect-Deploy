Q = 25
D = 10
N = 5
P = 1
print("Please enter an amount in cents less than a dollar.")
cents = int(input())
#num of quarters
Num_quarters = cents // Q
cents = cents % Q

#Dimes
Num_dimes = cents // D
cents = cents % D

#nickels
Num_nickels = cents // N
cents = cents % N

# Pennies
Num_pennies = cents // P
cents = cents % P

print("Your change will be:")
print(f"Q: {Num_quarters}")
print(f"D: {Num_dimes}")
print(f"N: {Num_nickels}")
print(f"P: {Num_pennies}")
