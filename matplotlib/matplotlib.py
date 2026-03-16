import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

#SCATTER PLOT
roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
marks=[76,39,80,12,23,48,51,94,65,7,10,92,38,74,56,65,47,83,29,1]

plt.figure(figsize=(8,4))
plt.scatter(roll_no,marks,color='red',marker='*')
plt.xlabel('Roll No.')
plt.ylabel('Marks')
plt.title('STUDENT MARKS')
plt.show()

#more functions
plt.figure(figsize=(8,5))
plt.plot(roll_no,marks,'bo',markersize=25)
plt.show()
plt.plot(roll_no,marks,'gv',markersize=18)
plt.show()

#multiple plots on single figure
temp1=[34,5,73,25,39,48,10,47]
hum1=[47,30,58,18,49,8,25,60]
temp2=[84,93,27,36,2,74,29,31]
hum2=[89,74,96,62,13,41,40,53]
plt.figure(figsize=(8,4))
plt.scatter(temp1,hum1,color='violet',marker='v')
plt.xlabel('TEMPERATURE CITY 1')
plt.ylabel('HUMIDITY CITY 1')
plt.title('WEATHER REPORT-CITY 1')
plt.show()

plt.xticks(np.arange(0,100,5))
plt.yticks(np.arange(0,100,5))
plt.plot(temp1,hum1,color='aqua',marker='^',markersize=10)
plt.plot(temp2,hum2,color='violet',marker='o',markersize=10)
plt.xlabel('TEMPERATURE CITY 1')
plt.ylabel('HUMIDITY CITY 1')
plt.title('WEATHER REPORT-CITY 1')
plt.show()

#using dataset
df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S5_Person_Data_Concept.csv')
print("dataset:\n",df)
plt.scatter(df['Height'],df['Index'],alpha=0.4)
plt.show()

#LINE PLOT
roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
marks=[76,39,80,12,23,48,51,94,65,7,10,92,38,74,56,65,47,83,29,1]
plt.plot(roll_no,marks,linestyle='-',color='purple',linewidth=10)    #linestyle=dashed,dotted,solis,dashdot,None
plt.show()

#multiple plots on same graph
plt.figure(figsize=(8,6))
plt.xticks(np.arange(0,100,5))
plt.yticks(np.arange(0,100,5))
plt.plot(roll_no,marks,linestyle='dotted',color='orange')
plt.show()

plt.figure(figsize=(8,6))
plt.xticks(np.arange(0,100,5))
plt.yticks(np.arange(0,100,5))
plt.plot(roll_no,marks,'wo')
plt.plot(roll_no,marks,'r-')
plt.show()

#BAR PLOT
name=['Louis','Pani','Ria','Cyril','Chris','Mani']
marks=[12,48,51,94,65,7]
plt.bar(name,marks,color='yellow',width=0.6,edgecolor='orange',linewidth=4,linestyle='solid')  #also -.
plt.show()

colors=['aqua','purple','orange','brown','violet','grey']
plt.bar(name,marks,color=colors)
plt.show()
#plt.barh(name,marks,color='yellow',width=0.6,edgecolor='orange',linewidth=4,linestyle='-.') -->horizontal version

#one over another 
name=['Louis','Pani','Cyril','Chris','Mani']
marks1=[12,48,51,94,7]
marks2=[47,62,19,50,88]
plt.bar(name,marks1)
plt.bar(name,marks2)
plt.show()

#alternate method to implement it correctly
name_len=np.arange(len(name))
width=0.4
plt.bar(name_len,marks1,width=width,color=colors)
plt.bar(name_len+width,marks2,width=width,color=colors,alpha=0.4)
plt.show()

#using dataset
df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S5_Person_Data_Concept.csv')
plt.bar(df['Index'],df['Height'],color='aqua')
plt.show()

#HISTOGRAMS
marks_50stud=np.random.randint(0,100,(50))
print("Marks:\n",marks_50stud)
plt.hist(marks_50stud)
plt.show()

bins=np.arange(0,100,5)
plt.hist(marks_50stud,bins=bins,color='purple',rwidth=0.6) #also add orientation='horizontal'-->that time, change the xticks to yticks
plt.xticks(np.arange(0,100,5))
plt.show()

#types of histogram---->step
plt.hist(marks_50stud,bins=bins,color='purple',histtype='step') 
plt.xticks(np.arange(0,100,5))
plt.show()

#two plot in same graph
marks_50stud1=np.random.randint(0,100,(50))
marks_50stud2=np.random.randint(0,100,(50))
bins=np.arange(0,100,5)
plt.figure(figsize=(6,6))
plt.hist([marks_50stud1,marks_50stud2],bins=bins,color=['violet','red'])
plt.xticks(np.arange(0,100,5))
plt.show()

#PIE CHAT OR PIE PLOT
name=['Louis','Panimalar','Ria','Cyril','Chris','Mani']
marks=[12,48,51,94,65,7]
colors=['red','violet','orange','yellow','aqua','green']
explode_values=[0,0,0,0.2,0,0]
textprops={'fontsize':9,'color':'k'}
wedgeprops={'linewidth':1,'linestyle':'solid','edgecolor':'white'}

plt.pie(marks,labels=name,colors=colors,autopct='%0.2f%%',explode=explode_values,shadow=True,radius=1,textprops=textprops,wedgeprops=wedgeprops)   #shadow-->by default=False
plt.title("Students Marks Report")
plt.legend()
plt.show()

#using dataset
df=pd.read_csv('D:/File Manager/DATA SCIENCE/Data Visualization/DS1_C4_S5_Revenue_Data_Concept.csv')
pie_df=pd.DataFrame(df['2020'].value_counts())
print("Value Count:\n",pie_df)
colors=['red','violet','orange','yellow','aqua','green','blue','pink','purple','brown']
plt.pie(df['2020'],labels=df.index,colors=colors,autopct='%0.1f%%')
plt.legend()
plt.show()

#SUBPLOTS
roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
marks=[76,39,80,12,23,48,51,94,65,7,10,92,38,74,56,65,47,83,29,1]
plt.scatter(roll_no,marks)
plt.show()
plt.plot(roll_no,marks)
plt.show()
plt.hist(marks)
plt.show()
plt.scatter(roll_no,marks,color='white')
plt.plot(roll_no,marks,'b-')
plt.show()

#all in one , by subplot
plt.figure(figsize=(7,7))
plt.subplot(2,2,1)
plt.scatter(roll_no,marks,color='aqua')

plt.subplot(2,2,2)
plt.plot(roll_no,marks,color='orange',linestyle='solid')

plt.subplot(2,2,4)
plt.hist(marks,color='red',edgecolor='yellow')

plt.subplot(2,2,3)
plt.scatter(roll_no,marks,color='white')
plt.plot(roll_no,marks,'b-')
plt.show()






































