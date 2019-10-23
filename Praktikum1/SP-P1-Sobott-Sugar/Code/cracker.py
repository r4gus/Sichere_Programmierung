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

def getPossibleTexts(cipher_text, char_pairs):
    """

    """
    l = []
    for cN, cE in char_pairs:
        a = (3 * (cN - cE)) % 26
        b = (cE - ( 4 * a )) % 26

        pt = acDecrypt(a, b, cipher_text)
        if pt != "":
            l.append(pt)

    return l


def getMostPossibleTexts(texts: list) -> list:
    """

    """
    word_list = make_word_list("commonEnglishWords.dic", 100)
    text_ranking = []
    for text in texts:
        counter = 0
        for word in word_list:
            counter += text.count(word)
        text_ranking.append((counter, text))
    text_ranking.sort(reverse=True)
    return text_ranking


def analyzeCipherText(cipher_text, char_pairs):
    """
    
    """
    texts = getPossibleTexts(cipher_text, char_pairs)
    sorted_texts = getMostPossibleTexts(texts)
    print(("\n\n".join(tup[1][:50] for tup in sorted_texts)))


   
def make_word_list(path: str, n: int) -> List[str]:
    with open(path, "r") as f:
        return [word.strip().lower() for word in f.read().split("\n") if word.strip()][:n]




if __name__ == "__main__":
    print(make_word_list("commonEnglishWords.dic", 20))
