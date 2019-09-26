# This program finds the nth term in the perrin sequence
# 
n = int(input("input n:"))
P = [3,0,2]
for i in range(n-2):
        P.append(P[i] + P[i+1])
print("The perrin sequence is", P)
                
                

        
        
	

