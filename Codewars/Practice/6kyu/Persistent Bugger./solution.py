def persistence(n):
    a = 0
    while n > 9:
        b = 1
        for i in str(n):
            b *= int(i)
        a += 1
        n = b
    return a
