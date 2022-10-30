'''
    @author Pratyay Ganguli
'''

'''

scoreCard = [
  [runs, overs, wickets]
]

'''

scoreCard = [
    [23, 1.3, 3],
    [20, 2.3, 2]
]

# list containing runs

def getRuns(scoreCard):
    runs = 0
    for session in scoreCard:
        runs = runs + session[0]
    print(runs)


# list containing overs balled

def getOvers(scoreCard):
    overs = 0.0
    for session in scoreCard:
        overs = overs + session[1]
    print(overs)


# list containing wickets

def getWickets(scoreCard):
    wickets = 0
    for session in scoreCard:
       wicktets = wickets + session[2]
    print(wicktets)


getRuns(scoreCard)
getOvers(scoreCard)
getWickets(scoreCard)
