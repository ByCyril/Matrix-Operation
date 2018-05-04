import math

def getProduct(matrixA, matrixB):
    matrixAB = []

    aRows = len(matrixA)
    aColumns = len(matrixA[0])
    bRows = len(matrixB)
    bColumns = len(matrixB[0])

    ax = 0
    bx = 0

    ay = 0
    by = 0

    matrixABSize = aRows * bColumns

    flag = 0

    tempA = []
    tempB = []
    temp = []

    if aColumns == bRows:

        while flag < matrixABSize:

            if bx < len(matrixA[ax]):
                tempA.append(matrixA[ax][bx])
                tempB.append(matrixB[ay][by])

                ay += 1
                bx += 1
            else:
                temp.append(getSum(tempA, tempB))

                if len(temp) == bColumns:
                    matrixAB.append(temp)
                    temp = []

                by += 1
                ay = 0
                bx = 0
                tempA = []
                tempB = []

                if by == bColumns:
                    by = 0
                    ax += 1
                
                flag += 1
    else:
        print("Matrix is not balanced")

    for columns in matrixAB:
        print(columns)


def getSum(arrayA, arrayB):

    sum = 0

    for i in range(0, len(arrayA)):
        sum = sum + (arrayA[i] * arrayB[i])

    return sum


A = [[-2, 1, 6],
     [6, -3, -3],
     [-1, 8, 3]]

B = [[4],
     [2],[2]]


getProduct(A, B)










