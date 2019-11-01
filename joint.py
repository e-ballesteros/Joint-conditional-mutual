#!usr/bin/env python3


# function that returns the joint entropy of two discrete random variables
def joint_entropy(pdf):                 # pdf is the joint p.d.f. of the discrete random variables

    from numpy import log2 as log2

    joint_ent = 0

    for i in range(0, len(pdf)):

        if pdf[i] != 0:
            joint_ent -= pdf[0] * log2(pdf[0])

    return joint_ent


