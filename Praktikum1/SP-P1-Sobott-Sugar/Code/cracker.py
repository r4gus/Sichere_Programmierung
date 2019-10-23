from typing import List, Dict

from aclib import encode, acDecrypt


def computeFrequencyTable(char_list: List[int]) -> Dict[int, int]:
    """ 
    Computes how often each character occures
    in the given 'List'.

    """
    table = {}
    for i in char_list:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    return table


def printFrequencyTable(table: Dict[int, int]) -> None:
    """ 
    Outputs a formated table of word:freq pairs.

    """
    print("\n".join([f"{encode([char])}: {freq}" for char, freq in table.items()]))


def computeMostFrequentChars(freq_table: Dict[int, int], n: int) -> List[int]:
    """
    Returns a list of the 'n' most frequent characters. 

    """
    l = [(freq, char) for char, freq in freq_table.items()]
    l.sort(reverse=True)
    l_cut = l[0:n]
    final = [tup[1] for tup in l_cut]
    return final
    # return [tup[1] for tup in sorted([(freq, char) for char, freq in freq_table.items()], reverse=True)[0:n]]
    

def computeKeyPairs(char_list: List[int]) -> List[int]:
    """
    L = {(a,b) | a, b e List ^ a != b}

    """
    final = []
    for char in char_list:
        for char2 in char_list:
            if char != char2:
                final.append((char, char2))
    return final


def analyzeCipherText(cipher_text, char_pairs):
    """
    
    """
    for cN, cE in char_pairs:
        a = (3 * (cN - cE)) % 26
        b = (cE - ( 4 * a )) % 26

        print(a, b)

        pt = acDecrypt(a, b, cipher_text)
        if pt != "":
            print(pt[:50])




if __name__ == "__main__":
    table = computeFrequencyTable([1, 22, 3, 22])
    printFrequencyTable(table)
    print(computeMostFrequentChars(table, 2))
    print(computeKeyPairs([13, 4, 19]))
