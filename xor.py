


def xor(a,b):
    """
    xorир по байтам

    >>> xor('1', '1')
    0
    """
    ia = int(a)
    ib = int(b)
    return ia^ib


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

