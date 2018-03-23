

import math
import plotly as py
from plotly.graph_objs import *
from ProductOfMatrix import ProductOfMatrix



def sqrt(x):
	return x**(1/2)



# original = [[2, 3, 3, 5, 5, 6, 6, 5, 5, 3, 3, 2],[9, 9, 6, 6, 9, 9, 3, 3, 5, 5, 3, 3]]

original = [[2, 5, 5, 3, 3, 5, 5, 2], [7, 7, 6, 6, 3, 3, 2, 2]]

transformation = [[-1/2, sqrt(3)/2], [-sqrt(3)/2, -1/2]]















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


    original[0].append(original[0][0])
    original[1].append(original[1][0])

    org = Scatter(x = original[0], y = original[1])

    matrixAB[0].append(matrixAB[0][0])
    matrixAB[1].append(matrixAB[1][0])

    trace = Scatter(x = matrixAB[0], y = matrixAB[1])

    t = Scatter(x = [10], y = [10])
    tt = Scatter(x = [-1], y = [-1])

    data = Data([org, trace, t, tt])
    py.offline.plot(data, filename = 'basic-line.html')


def getSum(arrayA, arrayB):

    sum = 0

    for i in range(0, len(arrayA)):
        sum = sum + (arrayA[i] * arrayB[i])

    return sum







getProduct(transformation, original)











