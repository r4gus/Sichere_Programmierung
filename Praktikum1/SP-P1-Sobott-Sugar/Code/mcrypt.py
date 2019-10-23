def gcd(a, b):
    """
    Calculates the greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mul_inverse(n, m):
    """
    Calculates the multiplicative inverse n^-1 of n (mod m).

        def: n * n^(-1) = 1 (mod m)

    Returns:    n^-1 e [0,1,2..m-1] if there is exactly one multiplicative
                inverse (e.g. gcd(n, m) != 1), None otherwise.
    """
    if gcd(n, m) != 1:
        return None

    module = m
    x = 1
    y = 0
    q = []

    while m != 0:
        q += [n // m]
        (n, m) = (m , n % m)

    q.reverse()

    for t in q:
        _x = y
        _y = x - ( _x * t )
        x = _x
        y = _y

    return (x + module) % module

def key_table(m):
    """
    Returns a dictionary key table that contains
    all subkeys a e {0, 1, ..., m - 1} and their
    corresponding multiplicative inverses.

    For m >= 2

    Returns:    dictionary key table on success,
                None otherwise.
    """
    if not isinstance(m, int) or m < 2:
        return None

    d = dict()

    for i in range(m):
        i_neg = mul_inverse(i, m)

        if i_neg != None:
            d[i] = i_neg

    return d


if __name__ == '__main__':
    m = 38
    num = 75
    
    print("a^-1 of " + str(num) + " = " + str(mul_inverse(num, m)))
    print(key_table(26))
