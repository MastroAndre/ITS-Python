# Somma diagonale principale di una matrice
def sum_primary_diagonal(matrix: list[list]) -> int:

    sum: int = 0

    if not matrix:
        raise ValueError("Matrice non valida")
    
    else:
        for l in matrix:
            for n in l:
                if l.index(n) == matrix.index(l):
                    sum += n
    
    return sum

# Somma diagonale secondaria di una matrice
def sum_secondary_diagonal(matrix: list[list]) -> int:

    sum: int = 0

    i: int = len(matrix) - 1

    if not matrix:
        raise ValueError("Matrice non valida")
    
    else:
        for lst in matrix:
            sum += lst[i]
            i -= 1

        return sum
        




l1: list = [1, 2, 3, 4] 
l2: list = [5, 6, 7, 8] 
l3: list = [9, 10, 11, 12] 
l4: list = [13, 14, 15, 16]

mat: list[list] = [l1, l2, l3, l4]

print(sum_primary_diagonal(mat))
print(sum_secondary_diagonal(mat))