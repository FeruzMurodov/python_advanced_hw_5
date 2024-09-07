def fibonacci(n: int):
    result = [0, 1]
    for i in range(1, n):
        result.append(result[i - 1] + result[i])
    return result


print(fibonacci(15))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
# 2-solution
def fibonacci2(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*fibonacci2(15))
