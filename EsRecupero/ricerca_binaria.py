def ricerca_binaria(lista: list[int], n: int) -> bool:

    sx: int = 0
    dx: int = len(lista) - 1

    while sx <= dx:
        medio: int = (sx + dx) // 2

        if lista[medio] == n:
            return True
        
        elif lista[medio] < n:
            sx = medio + 1

        else:
            dx = medio - 1
    
    return False


print(ricerca_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))