def Sprial(n):
    mat = [[0] * n for i in range(n)]
    rs , cs = 0 , 0
    re , ce = n-1 , n-1
    count = 1
    while rs <= re and cs <= ce:
        for i in range(cs,ce+1):
            mat[rs][i] = count
            count += 1
        rs += 1
        for i in range(rs,re+1):
            mat[i][ce] = count
            count += 1
        ce -= 1
        if rs <= re :
            for i in range(ce,cs-1,-1):
                mat[re][i] = count
                count += 1
            re-= 1
        if cs <= ce :
            for i in range(re,rs-1,-1):
                mat[i][cs] = count
                count += 1
            cs += 1
    return mat
print(Sprial(3))
