def printM(A):
    for i in A:
        for j in i:
            print(j, end = " ")
        print("")

def GCD(a, b):
        while a % b:
            temp = b
            b = a % b
            a = temp
        return b

def LCD(a, b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    return a * b / GCD(a, b)

def columnLCD(A, n):
    column = []
    for i in range(n):
        column.append(A[i][0])
    res = LCD(column[0], column[1])
    for i in range(2, n):
        res = LCD(res, column[i])
    return res

def multiply(A, n, line, alpha, toDivide):
    for i in range(n):
        A[line][i] *= alpha
    toDivide.append(alpha)

def doElementary(A, n, unchanged, result, alpha):
    for i in range(n):
        A[result][i] += A[unchanged][i] * alpha

def changeLines(A, n, diel):
    line = 0
    while A[line][0] == 0:
        line += 1
    for i in range(n):
        A[0][i], A[line][i] = A[line][i], A[0][i]
    diel.append(-1)

def cutM(A, n):
    for i in range(n):
        del A[i][0]
    del A[0]

def simplifyM(A, n, diel, toDivide):
    for i in range(1, n):
        if A[i][0]:
            multiply(A, n, i, columnLCD(A, n) / A[i][0], toDivide)
            doElementary(A, n, 0, i, (-1) * columnLCD(A, n) / A[0][0])
    diel.append(A[0][0])

diel = []
toDivide = []
A = []
A.append(input().split())
n = len(A[0])
counter = 1
while counter < n:
    line = input().split()
    if len(line) != n:
        print("Incorrect input")
    else:
        A.append(line)
        counter += 1
        
for i in range(n):
    for j in range(n):
        A[i][j] = int(A[i][j])
        
for i in range(n, 1, -1):
    if columnLCD(A, i) == 0:
        diel.append(0)
        break
    if A[0][0] == 0:
        changeLines(A, i, diel)
    simplifyM(A, i, diel, toDivide)
    cutM(A, i)
det = A[0][0]
for i in diel:
    det *= i
for i in toDivide:
    det /= i
print("")
print("det =", det)
