n = int(input())
arr1 = []

for _ in range(n):
    a = list(input())
    arr1.append(a)

if arr1[0][0] == "*" or arr1[n - 1][n - 1] == "*":
    print(0)
else:
    arr2 = [[0] * n for _ in range(n)]

    if arr1[0][0] == ".":
        arr2[0][0] = 1

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == "*":
                arr2[i][j] = 0
            else:
                if i > 0:
                    arr2[i][j] += arr2[i - 1][j]
                if j > 0:
                    arr2[i][j] += arr2[i][j - 1]

    print(arr2[n - 1][n - 1])
