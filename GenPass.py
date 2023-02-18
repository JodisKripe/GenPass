#!/usr/bin/python3
# Recommended to be executed as `python3 GenPass.py` and not `./GenPass.py`

## Features
# -by Back Date by Year
# -bm Back Date by Months
# -bs Back Date by Season
# -oby Only Back Dated by Year
# -obs Only Back Dated by Season
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--backdateyear", "-by", help="Back Dates Years upto 'n' years. eg: if n=2 and current year is 2023, the tool will consider years 2021,2022 and 2023")
parser.add_argument("--backdateseason", "-bs", help="Back Dates Seasons upto 3 seasons. eg: if value is 2 and current season is Winter, the tool will consider seasons Summer, Fall and Winter.\nNote: This also accounts for the change in years with seasons as well.")
args = parser.parse_args()

allSeasons = ["Winter","Spring","Summer","Fall"]

Symbols = ["!","@","#","$"]
Years =[]
Seasons =[]
Months =[]
today = datetime.date.today()
currentYear = today.year
currentMonth = today.strftime("%b")    
currentSeason=""   
#print(today.month)
Years.append(currentYear)
Months.append(currentMonth)
if(today.month in [12]):
    Seasons.append("Winter")
    currentSeason="Winter"
    Years[0]-=1
elif(today.month in [1,2]):
    Seasons.append("Winter")
    currentSeason="Winter"
elif(today.month in [3,4,5]):
    Seasons.append("Spring")
    currentSeason="Spring"
elif(today.month in [6,7,8]):
    Seasons.append("Summer")
    currentSeason="Summer"
elif(today.month in [9,10,11]):
    Seasons.append("Fall")
    Seasons.append("Autumn")
    currentSeason="Fall"

def flags():
    print(args)
    if(args.backdateyear):
        for i in range(1,int(args.backdateyear)+1):
            Years.append(int(currentYear)-i)
    if(args.backdateseason):
        ind = Seasons.index(currentSeason)
        for i in range(1,int(args.backdateseason)+1):
            if(ind-i<0):
                ind=3
                if(Years[0]-1 not in Years):
                    Years.append(Years[0]-1)
            else:
                ind=ind-1
            Seasons.append(allSeasons[ind])

def generateList():
    for i in Seasons:
        for j in Years:
            for k in Symbols:
                genpass1 = i + k + str(j)
                print(genpass1)
                genpass2 = i + str(j)[-2:] + k
                print(genpass2)


if(__name__=="__main__"):
    #print(Seasons,Years)
    flags()
    generateList()