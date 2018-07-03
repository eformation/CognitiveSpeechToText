import pandas as pd 
import sys
import seaborn as sb
from pylab import savefig
import convertCategoricalData as cat

def correlateddatframe():
	targetCol=""
	targetColFile=open("targetVariable.txt","r")
	for line in targetColFile:
		targetCol=line.split(" ")[0]
	#print(targetCol)


	df=cat.convertCategoricalData()
	corrMatrix=df.corr()
	sb.heatmap(corrMatrix)
	heatmap=sb.heatmap(corrMatrix) 
	figure=heatmap.get_figure()
	figure.savefig("Heatmap.png")
	#print(df.corr())
	#print(corrMatrix.axes[1][2])
	for i in range(0,len(corrMatrix.axes[1])):
		value=corrMatrix[targetCol][i]
		if(value >=-.3 and value <=0.3):
			df.drop(corrMatrix.axes[1][i],axis=1,inplace=True)	
			#print(df.head())
	return df

#dataframe=correlateddatframe()
#print(dataframe.head())



