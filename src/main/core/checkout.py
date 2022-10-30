'''
    @author Pratyay Ganguli
'''

# numberOfItems, amount

checkoutCart = [
    [2, 344.3],
    [1, 10.34],
    [5, 5003.24]
]

grossAmount = 0

for i in range(0, len(checkoutCart)):
    grossAmount = grossAmount + checkoutCart[i][1]

print(grossAmount)


