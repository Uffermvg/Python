
# This will calculate the resistance of a parallel and series resistors.
# 
def Rparallel(R1,R2):
	RP=1/((1/R1)+(1/R2))
	return RP
def Rseries (R1,R2):
		RS=R1+R2
		return RS
		
	
