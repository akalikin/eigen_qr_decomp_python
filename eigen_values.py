import numpy as np

THRESHOLD = 0.001

def main():
    file = open("in_matrix", "r")
    size = int(file.readline().strip("\n"))
    lines = file.read().split("\n")
    a = np.zeros(shape=(size,size))
    for i in range(size):
        a[i] = map(float, lines[i].split(" "))
    print("Input Matrix")
    print(a)
    e = eigen(a)
    print("Eigen Values")
    print(e)

def gs(inp):
    r = np.zeros(shape=(len(inp), len(inp)))
    q = np.zeros(shape=(len(inp), len(inp)))
    u = inp
    for k in range(len(u)):
        r[k][k] = sum([u[i][k]**2 for i in range(len(u))])**0.5 #magnitude : sqrt of sum of squares
        for i in range(len(u)):
            q[i][k] = u[i][k] / r[k][k]
        for j in range(k+1, len(u)):
            r[k][j] = sum([q[i][k] * u[i][j] for i in range(len(u))])
            for i in range(len(u)):
                u[i][j] -= r[k][j] * q[i][k]
    return q,r

def iteration(q,r):
    return np.dot(r, q)

def eigen(u):
    prev = np.zeros(shape=(len(u), len(u)))
    i = 0
    while(i < 50 and not diagonal(u, prev)):
        prev = np.copy(u)
        i+=1
        q,r = gs(u)
        u = iteration(q,r)
    return values(u)

def diagonal(u, prev):
    for i in range(len(u)):
        if abs(u[i][i] - prev[i][i]) > THRESHOLD:
            return False
    return True

def values(matrix):
    res = np.zeros(shape=(len(matrix)))
    for i in range(len(matrix)):
        res[i] = matrix[i][i]
    return res

if __name__ == '__main__':
    main()