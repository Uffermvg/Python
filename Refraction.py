# This will tell the final distnce after refraction
 
import math
N1N2 = eval(input("Please input indicies of refration here:"))
Angle = float(input("Please input incoming angle in degrees:"))
ListD = eval(input("Please input vertical distances here:"))
if (Angle > 90) :
	print ("Error")
elif (ListD[0]<=0):
        print ("Error")
elif (ListD[1] <= 0):
        print ("Error")
else:
	AngleRads = ((Angle*math.pi)/180)
	D4 = (math.tan(AngleRads) * ListD[0])
	Angle2 = (math.asin((N1N2[0] * math.sin(AngleRads))/N1N2[1]))
	D5 = (math.tan(Angle2) * ListD[1])
	D3 = D4 + D5
if (D3 < 0):
        print ("Error")
else :
        print ("Ending distances is", D3)






	

