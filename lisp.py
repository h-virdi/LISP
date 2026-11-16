def tokenize(text):
    text = text.replace("(", " ( ")
    text = text.replace(")", " ) ")
    return text.split()

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

def read_tokens(tokens):
    token = tokens.pop(0)
    if token == "(":
        curr = []
        while tokens and tokens[0] != ")":
            curr.append(read_tokens(tokens))
        if not tokens:
            raise SyntaxError("Missing")
        tokens.pop(0)
        return curr
    elif token == ")":
        raise SyntaxError("Unexpected")
    else:
        return atom(token)


def parse(text):
    return read_tokens(tokenize(text))
