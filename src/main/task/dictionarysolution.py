'''
    @author Pratyay Ganguli
'''


students = [
    {
        'branch': 'ECE',
        'enrollmentId': 223434773,
        'placed': True
    },
    {
        'branch': 'ME',
        'enrollmentId': 243334634,
        'placed': False
    },
    {
        'branch': 'CSE',
        'enrollmentId': 243335152,
        'placed': True
    }
]

def countPlaced(students):
    count = 0
    for student in students:
        if(student['placed']):
            count = count + 1

    return count