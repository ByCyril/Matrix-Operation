


def getDifference(matrixA, matrixB):

	matrixAB = []

	aRows = len(matrixA)
	aColumns = len(matrixA[0])

	bRows = len(matrixB)
	bColumns = len(matrixB[0])

	matrixABSize = aRows * bColumns

	temp = []

	if (aRows == bRows and aColumns == bColumns):

		ax = 0
		ay = 0
		bx = 0
		by = 0
		sum = 0

		for i in range(0, matrixABSize):

			sum = matrixA[ax][ay] - matrixB[bx][by]
			temp.append(sum)

			ay += 1
			by += 1

			if (len(temp) == aRows):
				matrixAB.append(temp)
				ay = 0
				by = 0
				ax += 1
				bx += 1
				temp = []

		for columns in matrixAB:
			print(columns)


a = [[1, 1], [1, 1]]
b = [[2, 3], [4, 5]]

getDifference(a, b)


