

def determinant3x3(A):

    r1 = A[0]
    r2 = A[1]
    r3 = A[2]

    i = r1[0] * ((r2[1] * r3[2]) + (r2[2] * r3[1]) )   
    j = r1[1] * ((r2[0] * r3[2]) + (r2[2] * r3[0]) )   
    k = r1[2] * ((r2[0] * r3[1]) + (r2[1] * r3[0]) )

    return i - j + k

#def determinant2x2(A):
    
    
a = [[1, 2, 3], [4, 5, 6], [3, 2, 1]]

print(determinant3x3(a))
