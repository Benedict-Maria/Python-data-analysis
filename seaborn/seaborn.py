import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
marks=[76,39,80,12,23,48,51,94,65,7,10,92,38,74,56,65,47,83,29,1]
df=pd.DataFrame({"Roll_No.":roll_no,"Marks":marks})
print("Sample data:\n",df)

#LINE PLOT
sns.lineplot(x='Roll_No.',y='Marks',data=df)
plt.title("Student Marks")
plt.xlabel("Student Roll_no")
plt.ylabel("Marks")
plt.show()

#using dataset
#seaborn_df=sns.load_dataset('DS1_C4_S5_Sales_Data_Concept')   -->possible in Google colab
seaborn_df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S5_Person_Data_Concept.csv')
#print("\ndataset:\n",seaborn_df)
sns.lineplot(x='Weight',y='Gender',data=seaborn_df)
plt.title('Person_Data')
plt.show()

sns.lineplot(x='Weight',y='Index',data=seaborn_df,hue='Height')
plt.title('Person_Data')
plt.show()

plt.figure(figsize=(10,10))
sns.lineplot(x='Height',y='Weight',data=seaborn_df,hue='Gender',style='Index')
plt.title('Person_Data')
plt.show()

sns.lineplot(x='Height',y='Index',data=seaborn_df,hue='Weight',style='Gender',legend=False)
plt.title('Person_Data')
plt.show()

sns.lineplot(x='Height',y='Weight',data=seaborn_df,hue='Gender',style='Index',legend='full',palette='flare') #by default legend=full  use any type of palette=crest
plt.title('Person_Data')
plt.show()

#DIST PLOT
df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S5_Person_Data_Concept.csv')
sns.distplot(df['Height'])
plt.show()

bins=[0,1,2,3,4,5]   #should be upto the specifying column name value , at here it is INDEX
sns.distplot(df['Index'],bins=bins)    #-->shows how which ranges high 
plt.xticks(bins)
plt.show()

sns.distplot(df['Index'],bins=bins,kde=False)
plt.xticks(bins)
plt.show()

sns.distplot(df['Index'],bins=bins,hist=False)
plt.xticks(bins)
plt.show()

sns.distplot(df['Index'],bins=bins,rug=True)
plt.xticks(bins)
plt.show()

sns.distplot(df['Index'],bins=bins,rug=True,color='orange',vertical=True
             #hist_kws={'color':'red','edgecolor':'blue','linewidth':4,'alpha':0.3},
             #kde_kws={'color':'green','linewidth':3,'alpha':0.4}
             )
plt.xticks(bins)
plt.show()

#SCATTER PLOT
sns.scatterplot(x='Weight',y='Height',data=df,hue='Gender',style='Index',palette='gist_rainbow',alpha=0.5)   #palette=inferno
plt.title('Person Data')
plt.show()

#scatter plot with line plot
sns.scatterplot(x='Index',y='Height',data=df,hue='Weight',style='Gender',palette='gist_rainbow',alpha=0.7)   #palette=inferno
sns.lineplot(x='Index',y='Height',data=df,color='blue')
plt.title('Person Data')
plt.show()

#BAR PLOT
sns.barplot(x='Gender',y='Height',data=df,hue='Index',palette='icefire')   #in output-->line indicates the uncertainity
plt.title('Person Data')
plt.show()

#orient and estimator 
sns.barplot(x='Weight',y='Gender',data=df,hue='Index',palette='Wistia',orient='h',estimator=np.mean)#orient-->'x' should be numeric. estimator can be max,min and so on.
plt.title('Person Data')
plt.show()

#confidence interval
sns.barplot(x='Gender',y='Height',data=df,hue='Index',palette='icefire',ci=100,errcolor='red',errwidth=5)  #ci-->indicates the size
plt.title('Person Data')
plt.show()

#saturation
sns.barplot(x='Gender',y='Height',data=df,hue='Index',palette='icefire',saturation=0.3)   #saturation from 0 to 1---->colourness
plt.title('Person Data')
plt.show()

#HEAT MAPS    -->flights dataset
#heat_df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S3_Loan_Data_Practice.csv.csv')
#heat_df=heat_df.pivot("Property_Area","Education","Loan_Amount_Term")
#print(heat_df.head())

#plt.figure(figsize=(12,6))
#ax=sns.heatmap(heat_df)
#print(ax)

#annot
#ax=sns.heatmap(heat_df,annot=True,fmt='d',linecolor='k',linewidth='5',cmap='red',cbar=False) --->annot=shows the values  cmap=shades of mentioning color
#print(ax)

#printing horizontally
#grid_kws={"height_ratios":(.4,.05),"hspace":.5}
#f,(ax,cbar_ax)=plt.subplot(2,gridspec_kw=grid_kws)
#ax=sns.heatmap(heat_df,cbar_kws={"orientation":"horizontal"},ax=ax,cbar_ax=bar_ax,)
#plt.show()

#another dataset--->titanic
#titanic_df=sns.load_dataset('titanic')
#print("\n",titanic_df.corr())
#sns.heatmap(titanic_df.corr())   -->gives correlation
#plt.show()







