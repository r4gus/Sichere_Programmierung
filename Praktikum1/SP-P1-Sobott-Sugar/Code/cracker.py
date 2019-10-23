from typing import List, Dict

from aclib import encode


def computeFrequencyTable(char_list: List[int]) -> Dict[int, int]:
    """ 
    
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
    """
    print("\n".join([f"{encode([char])}: {freq}" for char, freq in table.items()]))


def computeMostFrequentChars(freq_table: Dict[int, int], n: int) -> List[int]:
    """

    """
    l = [(freq, char) for char, freq in freq_table.items()]
    l.sort(reverse=True)
    l_cut = l[0:n]
    final = [tup[1] for tup in l_cut]
    return final
    # return [tup[1] for tup in sorted([(freq, char) for char, freq in freq_table.items()], reverse=True)[0:n]]
    


if __name__ == "__main__":
    table = computeFrequencyTable([1, 22, 3, 22])
    printFrequencyTable(table)
    print(computeMostFrequentChars(table, 2))
