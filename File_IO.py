
#  This program adds line numbers to a file
# 
userfile = input("Enter the filename of the input file:")
userfile1 = input("Enter the file name of the output file:")

inputfile = open(userfile , "r")
contents = inputfile.readlines()
inputfile.close()
string = ""

for i in range(len(contents)):
    string = (string + "{0:.0f} : ".format(i+1) + contents[i])

outputfile = open(userfile1 , "w+")
outputfile.write(string)
outputfile.close()

	
	




 

  
	

