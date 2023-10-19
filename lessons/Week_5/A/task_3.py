def add_to_table(table_1: list, table_2: list) -> None:
    # Check if they have the same dimensionality
    if len(table_1) != len(table_2) or len(table_1[0]) != len(table_2[0]):
        raise Exception("ERROR: They need to be the same length")

    # Define rows and columns
    rows, cols = len(table_1), len(table_1[0])
    
    # Define the computed array
    computed = [[0 for i in range(cols)] for i in range(rows)]

    # do the sum 
    for r in range(rows):
        for c in range(cols):
            computed[r][c] = table_1[r][c] + table_2[r][c]

    return computed

print(add_to_table([[1,2,3,4], [6,3,2,6],[7,8,9,0]], [[3,4,0,0], [3,1,0,1],[1,0,0,1]]))
