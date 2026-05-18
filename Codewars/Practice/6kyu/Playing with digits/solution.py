def dig_pow(n, p):
    numb = []
    owo = 0
    for i in str(n):
        numb.append(int(i))
    for i in numb:
        owo += i**p
        p += 1
    if owo % n == 0:
        return owo//n
    else:
        return -1
