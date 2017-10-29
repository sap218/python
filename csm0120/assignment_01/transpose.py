

def transpose(data):
    """A function to transpose a list of lists"""
    transposed = [list(x) for x in zip(*data)]
    return transposed

