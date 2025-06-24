from string import punctuation 

def count(text: str) -> dict[str, int]:

    d: dict[str, int] = {}

    l_text: str = text.lower()

    tokens: list[str] = l_text.split(" ")

    for token in tokens:
        c_token:str = ""

        for c in token:
            if c.isalpha():
                c_token += c

        if c_token in d:
            d[c_token] += 1

        else:
            d[c_token] = 1

    return d

print(count("Ciao, come stai? Ciao bene"))


