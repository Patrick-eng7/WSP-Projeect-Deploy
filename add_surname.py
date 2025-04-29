def add_surname(names):
    return [name + " Kardashian" for name in names if name.startswith("K")]
name_list = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
result = add_surname(name_list)
print(result)
