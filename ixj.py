i = int(input("i: "))
j = int(input("j: "))

matrix = [[0 for col in range(j)] for row in range(i)]

for row in range(i):
    for col in range(j):
        matrix[row][col]= i*j

print(matrix)