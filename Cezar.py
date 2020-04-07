
alp = 'abcdefghijklmnopqrstuvwxyz'
alph = alp.split()
def cezar(text, key):
    """
    шифрует по цезарю

    >>> cezar('nikita', 3)
    'qlnlwd'
    >>> cezar('nikita', 5)
    'snpnyf'

    """

    return ''.join(list(map(lambda i: i.replace(i, alp[alp.find(i)+key] ), text)))

def cezar_de(text, key):
    """
    дешифрует по цезарю

    >>> cezar_de('qlnlwd', 3)
    'nikita'
    >>> cezar_de('snpnyf', 5)
    'nikita'
    """
    return ''.join(list(map(lambda i: i.replace(i, alp[alp.find(i)-key] ), text)))

def analys(text):
    """
    Анализирует кол-во букв в процентах в слове

    """


    return {c:text.count(c) for c in set(text)}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
print(analys('nikita'))
