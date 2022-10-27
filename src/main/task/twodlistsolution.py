'''
    @author Pratyay Ganguli
'''


def getGrossSalary(employees):
    grossSalary = 0
    for employeeRecord in employees:
        grossSalary =grossSalary + employeeRecord[2]
    return grossSalary
