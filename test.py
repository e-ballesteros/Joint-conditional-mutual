from joint import joint_entropy

pdf = input('Introduce joint p.d.f. separated by commas: ')
numbers = list(map(float, pdf.split(',')))
value = joint_entropy(numbers)
print('The joint entropy is: ', value)
