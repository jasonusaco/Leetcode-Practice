def clearZero(mat,n):
    row = set()
    col = set()
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                row.add(i)
                col.add(j)
        for i in row:
            for j in range(n):
                mat[i][j] = 0
        for j in col:
            for i in range(n):
                mat[i][j] = 0
        return mat
