'''
    @author Pratyay Ganguli
'''

PLAN_TYPE = [
    "SUPER",
    "PREMIUM",
    "ULTRA_PREMIUM"
]

account = {
    "id" : "asca242e32edwdw4rf2342332dfeaxd",
    "username": "partha@gmail.com",
    "isMember": True,
    "plan": PLAN_TYPE[0],
    "password": "wef34r3f",
    "deviceIP": "192.124.34.32"
}

if account['plan'] == PLAN_TYPE[0]:
    print('Please upgrade!')
else:
    print('Do nothing')