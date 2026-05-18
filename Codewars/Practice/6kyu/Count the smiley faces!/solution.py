def count_smileys(arr):
    count = 0
    eyes = {':', ';'}
    noses = {'-', '~'}
    mouths = {')', 'D'}
  
    for i in arr:
        if len(i) == 2:
             if i[0] in eyes and i[1] in mouths:
                count += 1
        elif len(i) == 3:
            if i[0] in eyes and i[1] in noses and i[2] in mouths:
                count += 1
                
    return count
