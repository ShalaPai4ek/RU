def pig_it(text):
    words = text.split()
    result = []
    
    for w in words:
        if w.isalpha():
            new = w[1:] + w[0] + "ay"
            result.append(new)
        else:
            result.append(w)
    
    return " ".join(result)
 
