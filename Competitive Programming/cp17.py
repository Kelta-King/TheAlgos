def surfaceArea(A):
    
    h = len(A)
    w = len(A[0])
    area = 2*h*w

    for i in range(h):
        area += A[i][0]
    
    for i in range(h):
        area += A[i][w-1]
    
    for i in range(w):
        area += A[0][i]
    
    for i in range(w):
        area += A[h-1][i]
   
    for i in range(h):
        for j in range(w-1):

            area += abs(A[i][j] - A[i][j+1])
    
    for i in range(w):
        for j in range(h-1):

            area += abs(A[j][i] - A[j+1][i])
        
    return area

A = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
print(surfaceArea(A))