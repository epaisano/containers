

def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is None and c is None:
        result = -1
        i = 0
        while i < a:
            result += 1
            i += 1
            yield result
    if b is not None and c is None:
        result = a - 1
        i = a
        while i < b:
            result += 1
            i += 1
            yield result
    if b is not None and c is not None:
        if ((b < 0) and (c < 0)) or ((b > 0) and (c > 0)):
            result = a - c
            i = a
            while abs(i) < abs(b):
                result += c
                i += c
                yield result
        else:
            yield from ()
