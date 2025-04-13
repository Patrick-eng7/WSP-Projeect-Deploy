
num_count = int(input("How many integers would you like to enter?\n"))


print(f"Please enter {num_count} integers.")


first_number = int(input())
min_num = first_number
max_num = first_number


for _ in range(1, num_count):
    num = int(input())
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num


print(f"min: {min_num}")
print(f"max: {max_num}")
