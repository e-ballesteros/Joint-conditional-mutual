#!usr/bin/env python3


# function that returns the mutual information of two discrete random variables
def mutual_information(joint, marginal_x, marginal_y):

    from numpy import log2 as log2

    mutual_info = 0                                  # Mutual information of x and y

    for i in range(0, len(marginal_y)):
        for j in range(0, len(marginal_x)):
            if joint[i][j] != 0 and marginal_y[i] != 0 and marginal_x[j] != 0:
                mutual_info += joint[i][j] * log2(joint[i][j]/(marginal_y[i] * marginal_x[j]))

    return mutual_info
