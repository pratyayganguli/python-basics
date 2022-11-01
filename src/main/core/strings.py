'''
    @author Pratyay Ganguli
'''

message = 'hello pratyay'


if 'hello' in message:
    print('Greeting sent')

name = 'Pratyay'
name = name.replace('P', 'r')
print(name)

message = ' This message has a lot of blank spaces  '
print(message)
message = message.strip()
print(message)


age = 13
statement = 'She said her name was {2}, her age was {0} and her father was {1}.'.format(age, 'India', 'Pakistan')
print(statement)
