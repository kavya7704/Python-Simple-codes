def floodFill(image,sr,sc,color):
    n = len(image)
    m = len(image[0])
    
    original_color = image[sr][sc]

    def fill(sr, sc):
        image[sr][sc] = color
        for row, col in [[-1,0],[1,0],[0,-1],[0,1]]:
            delRow = sr + row
            delCol = sc + col
            if 0 <= delRow < n and 0 <= delCol < m and image[delRow][delCol] == original_color:
                fill(delRow, delCol)

    if image[sr][sc] != color:
        fill(sr, sc)

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
