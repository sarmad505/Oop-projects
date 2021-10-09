M = []
noOfRows = int(input("enter row value: "))
noOfColumns = int(input("enter column value: "))
for i in range(noOfRows):
    R = []
    for j in range(noOfColumns):
        element = int(input(f"enter number {j+1} "))
        R.append(element)
    M.append(R)

def displayMatrix():
    for i in range(noOfRows):
        for j in range(noOfColumns):
            print("%10.3f" % M[i][j],end ="\t")
        print()
displayMatrix()

pivotRow = int(input("Enter pivot row number: "))
pivotColumn = int(input("Enter pivot column number: "))
pivotRow -= 1
pivotColumn -=1

while (pivotRow >= 0 and pivotColumn >= 0):
    pivotElement = M[pivotRow][pivotColumn]
    for c in range(noOfColumns):
        M[pivotRow][c] = M[pivotRow][c]/pivotElement

        #displayMatrix()
    for r in range(noOfRows):
        if (r == pivotRow):
            continue
        if (r != pivotRow):
            pivotValue = M[r][pivotColumn]
        for c in range (noOfColumns):
            M[r][c] = M[r][c] -M[pivotRow][c] * pivotValue

    displayMatrix()


    pivotRow = int(input("Enter pivot row number: "))
    pivotColumn = int(input("Enter pivot column number: "))
    pivotRow -= 1
    pivotColumn -= 1


