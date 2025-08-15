n = int(input())

def Floyd(n):
    num = 1
    tri = []
    for i in range(1,n+1):
        row = []
        for j in range(1,i+1):
            row.append(num)
            num += 1
        tri.append(row)
    for row in tri:
        print(' '.join(map(str,row)))
Floyd(n)
