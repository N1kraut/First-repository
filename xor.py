


def xor(a,b):
    """
    xorир по байтам

    >>> xor('1', '1')
    0
    """
    ia = int(a)
    ib = int(b)
    return ia^ib
"""
def hexxor(a,b):

    xorрит хексовые

    >>>hexxor(110, 97)
    йцу

    qwe = hexlify(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(a), unhexlify(b))))
    return qwe
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
