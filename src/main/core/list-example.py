'''
    @author Pratyay Ganguli
'''

# Task to search an element in a list

# name = 'Pratyay Ganguli'
# print(name.__contains__('Ranguli'))

emailIds = [
    'pratyay@gmail.com',
    'partha@gmail.com',
    'james@gmail.com',
    'yeshwant@gmail.com',
]

# Searching (Linear Search) TimeComplexity - o(n)

def checkHotMails(emailIds):
    for i in range(0, len(emailIds)):
        if emailIds[i].__contains__('hotmail'):
            return True


    return False

print(checkHotMails(emailIds))

if checkHotMails(emailIds):
    print('Account found')
else:
    print('Not found')




