"""
Name: Kevin Li
UNI: krl2134
matrix_transpose returns the transpose of a given matrix, matrix_det returns 
the determinant of a given matrix, matrix_add returns the sum of two matrices,
and matrix_mult returns the matrix product of two matrices

"""
def matrix_transpose(matrix_A):
    #returns the transpose of a given matrix

    Ay = len(matrix_A)
    Ax = len(matrix_A[0])
    
    transposed_matrix = [[0 for i in range(Ay)] for j in range(Ax)]
    
    for y in range (0,len(matrix_A)):
        for x in range (0,len(matrix_A[y])):
            transposed_matrix[x][y] = matrix_A[y][x]
    return transposed_matrix


def matrix_det(matrix_A):
    #returns the determinant of a given 1x1 or 2x2 matrix

    Ay = len(matrix_A)
    Ax = len(matrix_A[0])
    
    determinant = 0
    
    if Ay != Ax:
        print("Cannot calculate determinant of a non-square matrix")
        return None
        
    elif len(matrix_A) > 2:
        print("Cannot calculate determinant of "\
        "a {}-by-{} matrix".format(Ay,Ax))
        return None
        
    elif Ay == 1:
        determinant = matrix_A[0]
        
    elif Ay == 2:
        determinant = matrix_A[0][0] * matrix_A[1][1] - \
        matrix_A[1][0] * matrix_A[0][1]

    return determinant

def matrix_add(matrix_A, matrix_B):
    #returns the sum of two matrices that are the same dimensions
    Ay = len(matrix_A)
    Ax = len(matrix_A[0])
    By = len(matrix_B)
    Bx = len(matrix_B[0])
    
    matrix_sum = [[0 for i in range(Ax)] for j in range(Ay)]
    
    if Ay != By or Ax != Bx:
        print("Cannot perform matrix addition between {}-by-{} matrix and "\
        "{}-by-{} matrix)".format(Ay,Ax,By,Bx))
        return None
        
    for y in range (0,Ay):
        for x in range (0,Ax):
            matrix_sum[y][x] = matrix_A[y][x] + matrix_B[y][x]
    
    return matrix_sum

def matrix_mult(matrix_A, matrix_B):
    #returns the matrix product of two matrices

    Ay = len(matrix_A)
    Ax = len(matrix_A[0])
    By = len(matrix_B)
    Bx = len(matrix_B[0])
    
    matrix_product = [[0 for i in range(Ay)] for j in range(Bx)]
    #initializes matrix of dimensions rows of A, cols of B
    
    if Ax != By:
        print("Cannot perform matrix multiplication between {}-by-{} matrix "
        "and {}-by-{} matrix".format(Ay,Ax,By,Bx))
        return None
        
    else:
        for a in range(0,Ay):
            for b in range(0,Bx):
                for c in range(0,Ax):
                    matrix_product[a][b] += matrix_A[a][c] * matrix_B[c][b]

    return matrix_product

if __name__ == '__main__':

    test_1 = [[1,9,-13],[20,5,-6]]
    test_2 = [[1,9],[20,5]]
    test_3 = [[4,8],[9,16]]

    print("Transpose Input:", test_1)
    print("Your transpose:", matrix_transpose(test_1))
    print("Expected transpose:", [[1,20],[9,5],[-13,-6]])

    print("Determinant Input:", test_2)
    print("Your determinant:", matrix_det(test_2))
    print("Expected determinant:", -175)

    print("Sum Input:", test_2, test_3)
    print("Your sum:", matrix_add(test_2, test_3))
    print("Expected sum:", [[5,17],[29,21]])

    print("Multiply Input:", test_2, test_3)
    print("Your product:", matrix_mult(test_2, test_3))
    print("Expected product:", [[85,152],[125,240]])
