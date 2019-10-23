import string
from mcrypt import gcd, key_table

alph_to_num = {k:v for v , k in enumerate(string.ascii_lowercase)}
num_to_alph = {v:k for v , k in enumerate(string.ascii_lowercase)}

def decode(text):
    """
    Takes a string as argument and converts every
    character to an corresponding integer, starting
    with 0.

    All special characters get lost through this transformation.
    
    e.g.    a -> 0
            b -> 1
            ...
            z -> 25
    """
    if not isinstance(text, str):
        raise AttributeError("Argument must be a str.")

    text = text.lower()
    
    return [ alph_to_num[c] for c in text if c in alph_to_num ]

def encode(int_list):
    """
    Takes a list of unsigned integers and converts every integer
    to an corresponding character, starting with a.

    Throws an KeyError exception if the list contains
    invalid values.

    e.g.    0 -> a
            1 -> b
            ...
            25 -> z
    """
    try:
        return "".join([ num_to_alph[d] for d in int_list ])
    except KeyError:
        raise AttributeError("Integer elements must be between 0 and 25.") 

def acEncrypt(a, b, plain_text):
    """
    Encrypt the specified plain_text using the affine cipher.

        y = (a*x +b)

    returns:    The cipher text on success,
                an empty string otherwise.
    """
    modulo = 26
    cipher_text = ""

    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(plain_text, str):
        print("[!!]: Invalid arguments. Must be: gcd(int, int, str)")
        return ""

    if gcd(a, modulo) != 1:
        print("[!!]: Invalid key 'a'. 'a' must be relatively prime to 26.")
        return ""
    
    t = decode(plain_text)
 
    for i in range(len(t)):
        t[i] = (a * t[i] + b) % modulo
    
    e = encode(t)
    return e.upper()




if __name__ == '__main__':
    print(acEncrypt(11, 23, "botschaft"))
