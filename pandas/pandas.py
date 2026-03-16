import pandas as pd
print(pd.__version__)

#PANDAS SERIES WITH PYTHON LIST
list=[1,2,3,4,5,6]
print("\nlist=",list)

series=pd.Series(list)
print("\nSeries=\n",series)
print("\nType:",type(series))

empty=pd.Series([])
print("\nEmpty:\n",empty)

a=pd.Series(['a','b','c','d','e'],index=[1,3,5,6,8])     #for generating own index
print("\na=",a)
a=pd.Series(['a','b','c','d','e'],index=[1,3,5,6,8],name='alphabets')     #for generating names 
print("\na=",a)

scalar_series=pd.Series(0.5)
print("\nScalar Series:",scalar_series)
scalar_series=pd.Series(0.5,index=[1,2,3,4])
print("\nScalar Series:",scalar_series)

#PANDAS SERIES WITH PYTHON DICTIONARY
dict_series=pd.Series({'p':1,'q':2,'r':3,'s':4,'t':5,'u':6})
print("\nDict_Series:",dict_series)
print("\ndict[0]=",dict_series[0])
print("\ndict[0:2]=",dict_series[0:2])
print("\nMax:",max(dict_series))
print("\nMin:",min(dict_series))

dict_series=pd.Series({'p':[1,2,3],'q':[4,5,6],'r':[7,8,9]})
print("\nDict Series:",dict_series)

#PANDAS DATAFRAMES
df=pd.DataFrame()
print("\nDataFrame:",df)

#DATAFRAME USING LIST
list=[1,2,3,4,5]
df=pd.DataFrame(list)
print("\nDataFrame:\n",df)

list=[[1,2,3,4,5],[6,7,8,9,10]]
df=pd.DataFrame(list)
print("\nDataFrame:\n",df)

#DATAFRAME USING DUCTIONARY--->REPRESENTS COLUMN NAMES
a=[{'a':3,'b':6,'c':9,'d':12,'e':15},{'a':10,'b':8,'c':6,'d':4,'e':2}]
df=pd.DataFrame(a)
print("\nDataFrame:\n",df)

#by using series
b={'Roll_No':pd.Series([100,101,102,103,104]),
   'Name':pd.Series(['Mia','Lisa','John','Lilly','Joseph']),
   'Total_Marks':pd.Series([90,89,78,67,56]),
   'Average':pd.Series([90.00,89.00,78.00,67.00,56.00])}
df=pd.DataFrame(b)
print("\nDataFrame using series:\n",df)

#READING CSV FILE AS DATAFRAMES
df=pd.read_csv("D:/File Manager/DATA SCIENCE/Data Visualization(youtube)/DS1_C4_S3_Loan_Data_Practice.csv.csv")
print("\nDataFrame:\n",df)
#print("\nDataFrame:\n",df.type)  

#operations
print("\nColumns:",df.columns)
print("\nShape:",df.shape)
print("\nSize:",df.size)
print("\nhead:\n",df.head())
print("\nTail:\n",df.tail())
print("\nDescribe:\n",df.describe())
print("\nInfo:",df.info())

#HANDLING NULL-VALUES OR MISSING-VALUES
print("\nIs-Null\n",df.isnull())
print("\nIs_Null-SUM:\n",df.isnull().sum())
print("\nIs-Null(TOTAL SUM):",df.isnull().sum().sum())

#DROPPING ROWS WITH NAN VALUES
print("\nshape\n",df.shape)
print("\ndropna\n",df.dropna())    #dropna()-->default axis=0(-->for rows)   we may also specify  dropna(axis=1 or 2...)
print("\ndropna\n",df.dropna(axis=1))    # axis=1--->for columns
print("\ndropna\n",df.dropna(how='any'))       #-->if any row value is null , then remove that row
print("\ndropna\n",df.dropna(how='all'))   #-->if all row value is null , then remove that row
print("\n",df.dropna(inplace=True))

#FILLING NULL-VALUES
#print(df.fillna(0))   #-->filling the missing value by specifying integer
#print(df.fillna({'column_name1':none,'column_name2':0,'column_name3':30(someother-ineger)}))-->for specific columns
#print(df.fillna(method='ffill'))-->forward fill
#print(df.fillna(method='ffill',axis=1))-->1=row    0=column
print("\nMean.fillna()",df['LoanAmount'].fillna(value=df['LoanAmount'].mean()))
#print(df.fillna(method='bfill'))-->backward fill
#print(df.fillna(method='ffill',inplace=True))    inplace=true-->replace the original value

#replace() function
#print("\nreplace()\n",df.replace(to_replace=360,value=240))  #or
#print("\nreplace()\n",df.replace(360,240))
#print("\nreplace()\n",df.replace(to_replace=[12,23,34,45,56,67,78,89,90],value='B'))
#print("\nreplace()\n",df['LoanAmount'].replace(to_replace=[12,34,45,78,89,90],value=['A','B','C','D','E','F']))
#print("\n",df.replace('[A-Za-z]',0))
#print("\n",df.replace('[A-Za-z]',0,regex=True))#-->regular exression(the values that change the null,values by alphabets,are changed to 0)
#print("\n",df.replace(to_replace=15,method='bfill'))
#print("\n",df.replace(to_replace=15,method='ffill'))

#loc()
#df1=pd.read_csv("D:/File Manager/DATA SCIENCE/Data Visualization(youtube)/DS1_C4_S3_Loan_Data_Practice.csv.csv",index_col=['Loan_ID'])
print("\nlocation:",df.loc[1])    #print 1st row details
print("\nlocation:",df.loc[[1,3,5,7]])
print("\n",df.loc[100,'Property_Area'])
print("\n",df.loc[100:114,'Education'])

df1=df.loc[df['ApplicantIncome']>5000]
print("\n",df1['Loan_ID'],df1['ApplicantIncome'])    #this can be done by following method
print("\n",df.loc[df['Loan_Amount_Term']>350,['Loan_ID']])   #GIVES ONLY SPECIFIED INDEX

#iloc()
print("\nindex location:",df.iloc[0])   #1st index values
print("\nindex location:",df.iloc[1])     #2nd index values
print("\nindex location:",df.iloc[[0]])   #in one line
print("\nindex location:",df.iloc[[1,2,3,4]])
print("\n",df.iloc[:,0])   #shows information of specific index number
print("\n",df.iloc[100:500,5])
print("\n",df.iloc[350:500,0:3])

#groupby() function
area_group=df.groupby(by='Property_Area')
print("\ngroupby()",area_group)
print("\ngroupbY() groups\n",area_group.groups)

area_loan=df.groupby(by=['Property_Area','Loan_Status'])
print("\ngroupbY() groups\n",area_loan.groups)

for group,data_frame in area_group:
    print("\nGroup:",group)
    print("\ndata_frame:\n",data_frame)

for group,data_frame in area_loan:
    print("\nGroup:",group)
    print("\ndata_frame:\n",data_frame)

#merge() function
df2=pd.DataFrame({'RollNo.':[1,2,3,4,5],'Name':['Cyril','Christa','Louis','Panimalar','Mani']})
print("\ndf2:\n",df2)
df3=pd.DataFrame({'RollNo.':[1,2,3,4,5],'Age':[19,15,55,45,4]})
print("\ndf2:\n",df3)
print("\nmerge():\n",pd.merge(df2,df3,on='RollNo.'))   #on-->by default intersecting column is taken

df2=pd.DataFrame({'RollNo.':[1,2,3,4,5],'Name':['Cyril','Christa','Louis','Panimalar','Mani']})
print("\ndf2:\n",df2)
df3=pd.DataFrame({'RollNo.':[1,2,7,4,8],'Age':[19,15,55,45,4]})
print("\ndf2:\n",df3)
print("\nmerge():\n",pd.merge(df2,df3))

print("\nmerge(left):\n",pd.merge(df2,df3,how='left'))
print("\nmerge(right):\n",pd.merge(df2,df3,how='right'))
print("\nmerge(outer):\n",pd.merge(df2,df3,how='outer'))

#append() function
df2=pd.DataFrame({'RollNo.':[1,2,3,4,5],'Name':['Cyril','Christa','Louis','Panimalar','Mani'],'Age':[19,15,55,45,4]})
df3=pd.DataFrame({'RollNo.':[6,7,8,9,10],'Name':['Cathreen','Chris','Lokesh','Malar','Mia'],'Age':[35,28,74,86,1]})
print("\ndf2:\n",df2)
print("\ndf3:\n",df3)

print("\nappend():\n",df2._append(df3))   #usually it's append()
print("\nappend(index=True):\n",df2._append(df3,ignore_index=True))

df2=pd.DataFrame({'RollNo.':[1,2,3,4,5],'Name':['Cyril','Christa','Louis','Panimalar','Mani']})
df3=pd.DataFrame({'RollNo.':[6,7,8,9,10],'Name':['Cathreen','Chris','Lokesh','Malar','Mia'],'Age':[35,28,74,86,1]})
print("\nappend():\n",df2._append(df3))   #filled with NAN values

#pivot table
#print("\npivot table:",pd.pivot_table(df,index='Property_Area')) -->groups based in index value and produce average values of other columns , only applicable to int64 datatype
#print("\npivot table:",pd.pivot_table(df,index='Property_Area',aggfunc='sum'))    #by defult it is avg, also we can find max,min,avg
#print("\npivot table:",pd.pivot_table(df,index='Property_Area',columns='Loan_Status'))  #groups based in index value ,also separates column wise









































