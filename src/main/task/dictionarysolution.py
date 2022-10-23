'''
    @author Pratyay Ganguli
'''

student = []

studentCollection = {

}

studentBloodGroups = [
    "A", "B", "B+", "O", "A", "B+"
]

studentCount = 0

for i in range(0, len(studentBloodGroups)):
    if studentBloodGroups[i] == 'B+':
        studentCount = studentCount + 1

print(studentCount)