from joint import joint_entropy
from conditional import conditional_entropy
from mutual_info import mutual_information
import numpy as np


in_string = input('Introduce marginal p.m.f. of X separated by commas: ')
pmf_x = list(map(float, in_string.split(',')))                              # Split input by commas into list in float

in_string = input('Introduce marginal p.m.f. of Y separated by commas: ')
pmf_y = list(map(float, in_string.split(',')))                              # Split input by commas into list in float

joint_pmf = np.zeros(shape=(len(pmf_y), len(pmf_x)))                        # Matrix with dimensions given by pdfs

print('Joint p.m.f. table')

for i in range(0, len(pmf_y)):                                              # Input of elements of joint pmf table
    for j in range(0, len(pmf_x)):
        joint_pmf[i][j] = float(input('Introduce element of row ' + str(i) + ' and column ' + str(j) + ': '))

# Printing results calling functions of joint.py, conditional.py and mutual_info.py
print('The joint entropy is: ', joint_entropy(joint_pmf))
print('The conditional entropy is [X|Y, Y|X]: ', conditional_entropy(joint_pmf, pmf_x, pmf_y))
print('The mutual information is: ', mutual_information(joint_pmf, pmf_x, pmf_y))

