import sys
import pandas as pd
import re
def convertCategoricalData():
	filepath=sys.argv[1]
	infoFile= open("Output.txt",'r') #list
	missingValueFile=open("MissingValueOutput.txt",'r')

	df=pd.read_csv(filepath)
	dfcount=len(df.axes[0])


	#print(df)
	
	#print("Total no of rows in the csv file",dfcount)

	## DROPPING COLUMNS VALUES WHICH HAS 70% DATA MISSING
	for row in missingValueFile:
		try:
			missingValue=row.split(" ")[-1]
			missingcolName=row.split(" ")[0]
			#print(missingValue,"***********")
			if((int(missingValue)/dfcount)>=0.7 and int(missingValue) !=0):
				#print("column which has 70% data missing",missingcolName)
				df.drop([missingcolName],axis=1,inplace=True)	
				#print(df)
			else:

				if(int(missingValue) !=0):
					minm=df[missingcolName].min()
					maxm=df[missingcolName].max()
					fill=int((minm+maxm)/2)
					#print(fill)
					#print(df.count())
					df[missingcolName].fillna(fill, inplace=True)
					#print(df.count())
					
				else:
					pass	
		except:
			pass	
	#DROPPING NAN VALUES BEFORE CATEGORIZING
	#df.dropna(inplace=True) #remove nan value before categorizing
	
	## LOOKING FOR STRING COLUMNS IN DATAFRAME, IF IT HAS 2-4 UNIQUES VALUES-> CONVERTING IT TO NUMERIC-> DROP ORIGNAL COLUMNS.  ELSE DROPPING THE STRING COLUMNS THAT CANT BE CATEGORIZED 	
	for lines in infoFile:
		try:
			#print(lines.split(" "))
			columnType=lines.split(" ")[-1]
			columnName=lines.split(" ")[0]
			#print(columnType,columnName)
			if (columnType.strip("\n") == "object"):
				#print(columnName)
				count=len(df[columnName].unique())
				#print(count)
				#print(type(df[columnName].unique()))
				#if(nan in df[columnName].unique().split(" ")):
					#count=count-1
					#print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
				#print(count)
				if(count>=2 and count<5):
					categDF=columnName+"Dummy"
					categDF = pd.get_dummies(df[columnName],drop_first=True)
					#print(categDF.head())
					df.drop([columnName],axis=1,inplace=True)
					df=pd.concat([df,categDF],axis=1)
					#print(df.head())
				else:
					df.drop([columnName],axis=1,inplace=True)
					#print(df.head())	
		except:
			pass

	return df		

convertedDataframe=convertCategoricalData()
#print(convertedDataframe.count())