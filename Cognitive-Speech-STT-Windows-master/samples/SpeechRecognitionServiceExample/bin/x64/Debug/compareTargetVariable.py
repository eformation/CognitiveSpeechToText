import sys

targetVar=sys.argv[1]
flag=0
infoFile= open("Output.txt",'r')
#print(targetVar)

for lines in infoFile:
	#print(lines.split(" ")[0])
	if (lines.split(" ")[0]).lower()==targetVar.lower():
		print("Found")
		with open("targetVariable.txt", "w") as text_file:
   	   	 text_file.write(targetVar)
		flag=1
		break
	else :
		pass
if(flag==0):
	print("Not Found")		
			
		

