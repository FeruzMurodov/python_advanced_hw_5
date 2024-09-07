names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = {item[0]: item[1] * float(item[2].replace('%', '')) / 100 for item in list(zip(names, salary, bonus))}
print(result)
