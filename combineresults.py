import os
import pandas as pd
import json

myData=pd.DataFrame(columns=[ 'count'], index=["rule"])
with open('summary.csv') as f:
	lines=f.readlines()
	for line in lines:
		x_dict=json.loads(line)
		x_df=pd.DataFrame([x_dict]).transpose()
		#assign column names and set index
		x_df.columns=["count"]
		x_df.index.name="rule"
		myData=myData.append(x_df, ignore_index=False)

myData['rule1']=myData.index
grouped=myData['count'].groupby(myData['rule1'])
grouped=grouped.sum()
grouped.to_csv('summaryout.csv')
