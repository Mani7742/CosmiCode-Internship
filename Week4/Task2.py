#  Write a program to perform matrix multiplication for two given matrices.
def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.
    Returns the resulting matrix.
    Assumes A and B are lists of lists and dimensions are compatible.
    """
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Number of columns in A must equal number of rows in B.")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example usage:
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    product = matrix_multiply(A, B)
    print("Result of matrix multiplication:")
    for row in product:
        print(row)