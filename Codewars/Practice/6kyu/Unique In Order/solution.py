def unique_in_order(sequence):
    uniq = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            uniq.append(sequence[i])
    print(uniq)
    return uniq
