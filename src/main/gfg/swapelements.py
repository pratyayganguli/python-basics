'''
    @author Pratyay Ganguli
'''

numbers = [
    1, 3, 2, 5, 6
]

firstElement = numbers[0]
lastElement = numbers[len(numbers) - 1]

# swap operation

temp = firstElement
firstElement = lastElement
lastElement = temp

numbers[0] = firstElement
numbers[len(numbers) - 1] = lastElement

print(numbers)