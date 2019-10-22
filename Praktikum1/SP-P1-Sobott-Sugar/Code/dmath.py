def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def x_eucledian(n, m):
    """
    Calculates the multiplactive inverse of n.
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
        print(x , y)

    return (x + module) % module

    

    
    

if __name__ == '__main__':
    m = 19
    num = 5
    
    print("a^-1 of " + str(num) + " = " + str(x_eucledian(num, m)))
