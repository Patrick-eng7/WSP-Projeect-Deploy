num = int(input("Please enter a positive integer: "))
print(f"The factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
