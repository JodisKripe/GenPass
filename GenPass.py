#!/usr/bin/python3
# Recommended to be executed as `python3 GenPass.py` and not `./GenPass.py`

## Features
# -by Back Date by Year
# -bs Back Date by Season
# -oby Only Back Dated by Year
# -obs Only Back Dated by Season
import datetime

Years =[]
Seasons =[]

def initialise():    
    today = datetime.date.today()
    currentYear = today.year
    #print(today.month)
    Years.append(currentYear)
    if(today.month in [12,1,2]):
        Seasons.append("Winter")
    elif(today.month in [3,4,5]):
        Seasons.append("Spring")
    elif(today.month in [6,7,8]):
        Seasons.append("Summer")
    elif(today.month in [9,10,11]):
        Seasons.append("Fall")
        Seasons.append("Autumn")


if(__name__=="__main__"):
    initialise()
    print(Seasons,Years)