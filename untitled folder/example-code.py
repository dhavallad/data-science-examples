__author__ = 'fengchen'


from cvxopt import matrix, solvers, spmatrix
import numpy as np
import matplotlib.pyplot as plt
from math import *

def main():
    data = [[6.0,7,1], [7,7,1], [3,5,-1], [4,5,-1]]
    Q = spmatrix(2.0, range(3), range(3))
    print "EX Ma"
    EX = spmatrix(-1.0, range(5), range(5))
    print EX
    # print EX[1,1]
    for i in range(len(EX)):
        for j in range(len(EX)):
            print EX[i,j]




    print "Q mattix"
    Q[2,2] = 0
    print Q
    p = matrix([0.0, 0.0, 0.0], (3,1))
    G = []
    h = []


    print "G : [[-6.0, -7, -1], [-7, -7, -1], [3, 5, 1], [4, 5, 1]]"
    for items in data:
        row = []
        if items[2] == 1:
            row.extend([-1 * item for item in items[:2]])
            row.append(-1)
            # for i in range(len(EX)):
            #     for j in range(len(EX)):
            #         # print EX[0,i]
            #         row.append(EX[i,j])
            G.append(row)
            # G.append((EX[:5]))
            h.append(-1.0)
        else:
            row.extend(items[:2])
            row.append(1)
            # for i in range(len(EX)):
            #     print EX[0,i]
            #     row.append(EX[0,i])
            G.append(row)
            h.append(-1.0)
    print G
    for i in range(len(G)):
        for j in range(len(EX)):
            G[i].append(EX[i,j])




    G = matrix(G).trans()
    print "After transpsoe" 
    print G



if __name__ == '__main__':
    main()