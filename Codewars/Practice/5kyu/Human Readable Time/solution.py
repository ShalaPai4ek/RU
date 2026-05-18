def make_readable(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    
    return f"{h:02}:{m:02}:{s:02}"
