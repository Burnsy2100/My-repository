# Imports

import numpy as np

# Functions
def inputSizes():
    global nRows1
    global nColumns1
    global nRows2
    global nColumns2
    nRows1 = int(input("Enter number of rows for the first matrix/vector: "))
    nColumns1 = int(input("Enter number of columns for the first matrix/vector: "))
    nRows2 = int(input("Enter number of rows for the second matrix/vector: "))
    nColumns2 = int(input("Enter number of columns for the second matrix/vector: "))
    checkSizesValid()

def checkSizesValid():
    if nColumns1 == nRows2:
        enterValues()
    else:
        print("Cannot be multiplied!")

def enterValues():
    global m1
    global m2
    print("Matrix/Vector 1")
    m1 = [[0 for i in range(nColumns1)] for i in range(nRows1)]
    for rows in range(0, nRows1):
        for columns in range(0, nColumns1):
            tempNum = int(input("Enter number for row " + str(rows+1) + " column " + str(columns+1) + ": "))
            m1[rows][columns] = tempNum
            for i in range(0, len(m1)):
                print(m1[i])
    print("Matrix/Vector 2")
    m2 = [[0 for i in range(nColumns2)] for i in range(nRows2)]
    for rows in range(0, nRows2):
        for columns in range(0, nColumns2):
            tempNum = int(input("Enter number for row " + str(rows + 1) + " column " + str(columns + 1) + ": "))
            m2[rows][columns] = tempNum
            for i in range(0, len(m2)):
                print(m2[i])
    solveAndOutput()

def solveAndOutput():
    print("Result:")
    result = np.matmul(m1, m2)
    for i in range(0, len(result)):
        print(result[i])

# Main program

inputSizes()