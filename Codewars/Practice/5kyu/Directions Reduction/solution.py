def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for i in arr:
        if result and result[-1] == opposites.get(i):
            result.pop()
        else:
            result.append(i)
    
    return result
        
