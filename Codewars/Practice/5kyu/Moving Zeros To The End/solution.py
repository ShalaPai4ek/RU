def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    return non_zeros + zeros
