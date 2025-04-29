def without_duplicates(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list
my_list = [8, 'hello', 8, True, -1000000.4, 'hello', 8]
result = without_duplicates(my_list)
print(result)
