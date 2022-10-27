'''
    @author Pratyay Ganguli
'''

from src.main.task.twodlistsolution import *

employees = [
    ["Suraj", "Data Analyst", 500],
    ["James", "ML Engineer", 623.45],
    ["Gordon", "Accountant", 534.67]
]

print("Gross Salary is : {0}".format(getGrossSalary(employees)))

