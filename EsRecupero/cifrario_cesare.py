from string import ascii_lowercase

'''a, 2 = c'''

def caesar_cypher_encrypt(s: str, key: int) -> str:

    output: str = ""

    for carattere in s:

        if key <= 25:
            indice: int = ascii_lowercase.index(carattere)

            output += ascii_lowercase[indice + key]

        else:
            completo: int = key // 25

            indice: int = ascii_lowercase.index(carattere) - (25 * completo)

            output += ascii_lowercase[indice + key]

    return output



print(caesar_cypher_encrypt("abc", 2))