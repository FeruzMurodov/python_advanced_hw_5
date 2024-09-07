def pow_(n: int):
    for i in range(1, n + 1):
        yield i ** 2


print(*pow_(int(input("Enter a number: "))))

n = int(input("Enter a number: "))
print([x ** 2 for x in range(1, n + 1)])
