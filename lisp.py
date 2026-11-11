def tokenize(text):
    res = []
    for char in text:
        if char == " ":
            continue
        res.append(char)
    return res

def parse(text):
    ...