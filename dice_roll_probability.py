
# This will calculate the percent of wins and losses in a dice roll for different number of rolls.
# 
import random
number = [10,100,1000,10000,100000,1000000]
count = 0
Win = 0
Lose = 0
while count < number[0]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 10 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)
while count < number[1]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 100 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)
while count < number[2]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 1000 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)
while count < number[3]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 10000 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)
while count < number[4]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 100000 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)
while count < number[5]:
        roll = random.randint(1,6)
        count = count +1
        if roll >= 5 :
                Win = Win +1
        else :
                Lose = Lose +1
percentwin = (Win /(Lose + Win)) * 100
percentlose = (Lose /(Lose + Win)) * 100
print ("For 1000000 rolls")
print ("Percent Wins", percentwin, "Percent Losses", percentlose)





 

  
	

