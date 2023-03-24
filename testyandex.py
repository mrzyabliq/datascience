n, m, q = map(int, input().split())

dc = [[1] * m for i in range(n)]
dc1 = [m] * n
resets = [0] * n

def maxdc(arr2, arr3, k):
    max = 0
    m = -1
    for j in range(k):
        pr = arr3[j] * arr2[j]
        if pr > m:
            m = pr
            max = j + 1
    return max

def mindc(arr2, arr3, k):
    min = 1
    mi = arr3[0]*arr2[0]
    for j in range(k):
        pr = arr3[j] * arr2[j]
        if pr < mi:
            mi = pr
            min = j + 1
    return min

command = [input().split() for i in range(q)]

for i in range(q):
    if command[i][0] == "DISABLE":
        if dc[int(command[i][1]) - 1][int(command[i][2]) - 1] == 0:
            dc1[int(command[i][1]) - 1] -= 0
        else:
            dc[int(command[i][1]) - 1][int(command[i][2]) - 1] = 0
            dc1[int(command[i][1]) - 1] -= 1
            
    elif command[i][0] == "RESET":
        dc[int(command[i][1]) - 1] = [1] * m
        dc1[int(command[i][1]) - 1] = m
        resets[int(command[i][1]) - 1] += 1
        
    elif command[i][0] == "GETMAX":
        print(maxdc(resets, dc1, n))
        
    elif command[i][0] == "GETMIN":
        print(mindc(resets, dc1, n))



