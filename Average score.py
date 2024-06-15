grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student = {'Johnne', 'Bildo', 'Steve', 'Khendrik', 'Aaron'}
student = tuple({'Johnne', 'Bildo', 'Steve', 'Khendrik', 'Aaron'})
grades[0] = ((5 + 3 + 3 + 5 + 4) / 5)
grades[1] = ((2 + 2 + 2 + 3) / 4)
grades[2] = ((4 + 5 + 5 + 2) / 4)
grades[3] = ((4 + 4 + 3) / 3)
grades[4] = ((5 + 5 + 5 + 4 + 5) / 5)
Journal = {student[0]: grades[0], student[1]: grades[1], student[2]: grades[2], student[3]: grades[3], student[4]: grades[4]}
print(Journal)