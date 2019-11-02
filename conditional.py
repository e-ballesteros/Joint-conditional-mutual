#!usr/bin/env python3


# Function that returns the two possibles joint entropies of two discrete random variables
def conditional_entropy(joint, marginal_x, marginal_y):

    from numpy import log2 as log2

    conditional_ent_xy = 0                                  # Conditional entropy of x given y
    conditional_ent_yx = 0                                  # Conditional entropy of y given x

    for i in range(0, len(marginal_y)):
        for j in range(0, len(marginal_x)):
            if joint[i][j] != 0 and marginal_y != 0:        # If the probability is zero there is no need to calculate
                conditional_ent_xy -= joint[i][j] * log2(joint[i][j]/marginal_y[i])

    for i in range(0, len(marginal_y)):
        for j in range(0, len(marginal_x)):
            if joint[i][j] != 0 and marginal_x != 0:        # If the probability is zero there is no need to calculate
                conditional_ent_yx -= joint[i][j] * log2(joint[i][j]/marginal_x[j])

    return [conditional_ent_xy, conditional_ent_yx]
