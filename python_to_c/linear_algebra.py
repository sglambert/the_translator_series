def transpose_matrix(m):
    """
    Will transpose a matrix (list of lists)
    e.g.
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    will return matrixT = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    return map(list, zip(*m))


def matrix_minor(m,i,j):
    """
    A minor of a matrix, A, is the determinant of a smaller square matrix,
    cut down from A by removing one or more of its rows and columns.
    """
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def matrix_deternminant(m):
    #2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*matrix_deternminant(matrix_minor(m,0,c))
    return determinant


def matrix_inverse(m):
    determinant = matrix_deternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = matrix_minor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * matrix_deternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transpose_matrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
    """
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < cols:
            matrix[-1].append(0.0)

    return matrix


def identity_matrix(m):
    """
    Creates and returns an identity matrix.
    """
    id_matrix = zeros_matrix(m, m)
    for i in range(m):
        id_matrix[i][i] = 1.0

    return id_matrix

