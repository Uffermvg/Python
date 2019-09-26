
# This calculates the number of days and years needed to save a certain amount of money.
# 
Savings = int(input("input savings wanted"))
Balance = [1]
Cents = (Savings * 100)
Day = 0
while (Balance[Day] < Cents):
	Balance.append(Balance[Day] + Day)
	Day = Day + 1
print ("The number of days needed to save is", Day)
print ("The number of years needed to save is" , (Day/365))
print ("The final balance is", (Balance[Day]/100))
print ("The contribution on the final day is", (Day/100))
	


 

  
	

