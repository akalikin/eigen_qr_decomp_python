#credit - Artem Kalikin (ak7613@ic.ac.uk)
#Performs QR iterations using Gram-Schmidt Process
#until eigen values converge within a threshold
#prints eigenvalues rounded to 3 (PRECISION) decimal points

"""
input file format
first line - matrix dimension
then numbers divided by space
ex:
4
1 2 3 4
3 2 1 4
2 3 1 4
4 3 1 2
"""

import numpy as np
THRESHOLD = 0.001 #determines convergence
PRECISION = 3   #number of decimal points

def main():
    a = read_file("in_matrix")
    print("Input Matrix")
    print(a)
    e = eigen(a)
    print("Eigen Values")
    print(e)

#Opens file and fills the matrix with values from the file
#if file does not exist uses predefined matrix
def read_file(filename):
    try:
        file = open(filename)
        size = int(file.readline().strip("\n"))
        lines = file.read().split("\n")
        a = np.zeros(shape=(size,size))
        for i in range(size):
            a[i] = map(float, lines[i].split(" "))
    except IOError:
        print "Could not open file, using standard input matrix"
        a = [[1,2,3,4], [3,2,1,4], [2,3,1,4], [4,3,1,2]]
    return a

def gram_schmidt(inp):
    r = np.zeros(shape=(len(inp), len(inp)))
    q = np.zeros(shape=(len(inp), len(inp)))
    for k in range(len(inp)):
        r[k][k] = sum([inp[i][k]**2 for i in range(len(inp))])**0.5 #magnitude : sqrt of sum of squares
        for i in range(len(inp)):
            q[i][k] = inp[i][k] / r[k][k]
        for j in range(k+1, len(inp)):
            r[k][j] = sum([q[i][k] * inp[i][j] for i in range(len(inp))])
            for i in range(len(inp)):
                inp[i][j] -= r[k][j] * q[i][k]
    return q,r

def iteration(q,r):
    return np.dot(r, q)

#QR Iterations, If metrix does not converge - stops after 50 iterations
def eigen(inp):
    inp_prev = np.zeros(shape=(len(inp), len(inp)))
    iter = 0
    while iter < 50 and not diagonal(inp, inp_prev):
        inp_prev = np.copy(inp)
        iter+=1
        q,r = gram_schmidt(inp)
        inp = iteration(q,r)
    return values(inp)

#Checks for convergence, if difference in diagonal
# is less than THRESHOLD returns True
def diagonal(inp, inp_prev):
    for i in range(len(inp)):
        if abs(inp[i][i] - inp_prev[i][i]) > THRESHOLD:
            return False
    return True

#Returns eigen values - diagonal of the matrix
def values(matrix):
    res = np.zeros(shape=(len(matrix)))
    for i in range(len(matrix)):
        res[i] = round(matrix[i][i], PRECISION)
    return res

if __name__ == '__main__':
    main()