from joint import joint_entropy
from conditional import conditional_entropy
from mutual_info import mutual_information


in_string = input('Introduce marginal p.d.f. of X separated by commas: ')
pdf_x = list(map(float, in_string.split(',')))

in_string = input('Introduce marginal p.d.f. of Y separated by commas: ')
pdf_y = list(map(float, in_string.split(',')))

joint_pdf = [[]]

for i in range(0, len(pdf_y) - 1):
    for j in range(0, len(pdf_x) - 1):
        joint_pdf[i][j] = float(input('Introduce element of row', i, 'and column', j, ': '))

#joint_pdf = list(map(float, in_string.split(',')))

print('The joint entropy is: ', joint_entropy(joint_pdf))
print('The conditional entropy is: ', conditional_entropy(joint_pdf, pdf_x, pdf_y))
print('The mutual information is: ', mutual_information(joint_pdf, pdf_x, pdf_y))

