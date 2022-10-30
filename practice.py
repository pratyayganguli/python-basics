def data():
    return "print"
print(data())

def param():
    print("bayleaf")
param()

def validtweet(characters):
    if (characters <= 140):
        return "Valid Tweet"
    else:
        return "Not Valid Tweet"

print(validtweet(150))

def positivevibes(value):
    if (value >= 0):
        return "Good Vibes"
    else:
        return "Red Flag"
print(positivevibes(-98))

def bloodpressureH(Hg):
    if (Hg >= 130):
        return "High"
    elif (Hg <120):
        return "Low"
    else:
        return "Normal"
def bloodpressureL(Hg):
    if (Hg < 80):
        return "Low"
    elif (Hg >85):
        return "High"
    else:
        return "Normal"
print(bloodpressureH(135))
print(bloodpressureL(80))

students = [
{
    "branch" : "ME-B",
    "enrollmentID" : "1501061128",
    "placed" : True
},
{
    "branch" : "ME-B",
    "enrollment" : "1501061129",
    "placed" : True
},
{
    "branch" : "ME-B",
    "enrollment" : "1501061130",
    "placed" : False
},

    {
    "branch" : "ME-B",
    "enrollment" : "1501061131",
    "placed" : True}

]

employees = [
    ["Suraj", "Data Analyst", 500],
    ["James","ML Engineer", 623.45],
    ["Gordon", "Accountant", 534.67]
]

