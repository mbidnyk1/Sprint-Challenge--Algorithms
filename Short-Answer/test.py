def q1(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
    return a

print(q1(1000000))