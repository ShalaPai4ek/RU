def generate_hashtag(s):
    s = '#' + s.title().replace(' ', '')
    if len(s) > 140 or len(s) == 1:
        return False
    else:
        return s
