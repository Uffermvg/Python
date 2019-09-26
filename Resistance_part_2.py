
# This will find the total resistance the voltage at each resistor and the current at each resistor of a parralel or series circit.
# 
ListR = eval(input("Please in put resistor values:"))
V = float(input("please input the voltage:"))
Type = int(input("Please input a 1 if the resistors are parrallel and a 0 if the resistors are in series:"))
if (ListR[0] < 0) : 
	print ("Error")
elif (ListR[1] < 0) :
	print ("Error")
elif  (Type == 0) :
	R = (ListR[0] +ListR[1])
	V1 = ((ListR[0] / (ListR[0] + ListR[1])) * V )
	V2 = ((ListR[1] / (ListR[0] + ListR[1] )) * V)
	I1 = ( V / R )
	I2 = I1
	print (" The total resistance is", R)
	print ("The voltage at the first resistor is", V1)
	print ("The voltage at the second resistor is", V2)
	print ("The curent at the first resistor is", I1)
	print ("The current at the second reisitor is" , I2)
elif (Type == 1) :
	R = (1/((1 / ListR[0]) + (1 / ListR[1]))) 
	I = ( V / R )
	I1 = ((ListR[1] / (ListR[0] + ListR[1])) * I)
	I2 = ((ListR[1] / (ListR[0] + ListR[1])) * I)
	V1 = V
	V2 = V 
	print (" The total resistance is", R)
	print ("The voltage at the first resistor is", V1)
	print ("The voltage at the second resistor is", V2)
	print ("The curent at the first resistor is", I1)
	print ("The current at the second reisitor is" , I2)
else :
	print ("error")





	

