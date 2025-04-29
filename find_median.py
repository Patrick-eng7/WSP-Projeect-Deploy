def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    middle = n // 2

    if n % 2 == 1:
        return numbers[middle]
    else:
        return (numbers[middle - 1] + numbers[middle]) / 2

some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)
