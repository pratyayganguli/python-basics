'''
    @author Pratyay Ganguli
'''

emailIds = ['p123@mail.com', 'p323@mail.com', 'p223@mail.com']
print(emailIds)

emailIds[2] = 'axs'
print(emailIds)

emailIds.append([1, 2, 3])
print(emailIds)

# Tuple

admins = ('partha', 'souvik', 'qwe')
admins = ('pratyay', 'argha')
print(admins)

imageResolutions = (
                        (122, 3344),
                        (222, 33),
                        (221, 456)
                    )

for i in range(0, len(imageResolutions)):
    print(imageResolutions[i])