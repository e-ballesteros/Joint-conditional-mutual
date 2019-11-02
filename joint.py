#!usr/bin/env python3


# function that returns the joint entropy of two discrete random variables
def joint_entropy(pdf):                 # pdf is the joint p.d.f. of the discrete random variables

    from numpy import log2 as log2
    import numpy as np

    joint_ent = 0
    dimensions = np.shape(pdf)

    for i in range(0, dimensions[0]):
        for j in range(0, dimensions[1]):
            if pdf[i][j] != 0:
                joint_ent -= pdf[i][j] * log2(pdf[i][j])

    return joint_ent


