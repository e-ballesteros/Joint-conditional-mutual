#!usr/bin/env python3


# function that returns the joint entropy of two discrete random variables
def joint_entropy(pmf):                                     # pdf is the joint p.d.f. of the discrete random variables

    from numpy import log2 as log2
    import numpy as np

    joint_ent = 0
    dimensions = np.shape(pmf)                              # Number of rows and columns of the joint pdf matrix

    for i in range(0, dimensions[0]):                       # Rows of matrix
        for j in range(0, dimensions[1]):                   # Columns of matrix
            if pmf[i][j] != 0:                              # If joint probability is zero there is no need to calculate
                joint_ent -= pmf[i][j] * log2(pmf[i][j])

    return joint_ent


