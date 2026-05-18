def rgb(r, g, b):
    rgb = [max(0, min(i, 255)) for i in (r, g, b)]
    return "{:02X}{:02X}{:02X}".format(*rgb)
