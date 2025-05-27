# Name: Patrick K.
# GitHub Username: Patrick-eng7
# Date: 5/27/2025
# Description: This program defines a function named dot_prod to compute the
#              dot product of two equal-length lists (vectors), and a function
#              named matrix_mult that multiplies two 2D matrices represented
#              as lists of lists. If the dimensions of the matrices are not
#              compatible for multiplication, matrix_mult returns None.

def dot_prod(vec1, vec2):
    """
    Compute and return the dot product of two vectors (lists of numbers).
    """
    if len(vec1) != len(vec2):
        return None  # dot product undefined if lengths differ

    return sum(a * b for a, b in zip(vec1, vec2))


def matrix_mult(A, B):
    """
    Multiply two matrices A and B and return the resulting matrix.
    Return None if the number of columns in A does not match
    the number of rows in B.
    """
    if len(A[0]) != len(B):
        return None  # Cannot multiply if dimensions don't align

    result = []

    # Transpose B to get its columns as rows for easier access
    transposed_B = list(zip(*B))

    for row_A in A:
        result_row = []
        for col_B in transposed_B:
            result_row.append(dot_prod(row_A, col_B))
        result.append(result_row)

    return result
