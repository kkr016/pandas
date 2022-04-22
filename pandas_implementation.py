# -*- coding: utf-8 -*-
"""pandas_implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GVVmE8cXXI_9fp5uJcV8_zGt3OpvB-j7

###### Assessment

###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

###### import necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

"""###### merge those two csv files (after getting as dataframes, get them as a single dataframe)"""

df1 = pd.read_csv("/content/college_1.csv")
df2 = pd.read_csv("/content/college_2.csv")

df1.head()

df2.head()

df3 = pd.concat([df1, df2], ignore_index=True)
print("\nThe new DataFrame: df3\n")
df3.head()

df3.tail()

"""###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo)

###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv

###### if  10000<codekata score<15000   (Reached_expectations.csv)

###### if  7000<codekata score<10000   (Needs_Improvement.csv)

###### if  codekate score < 7000        (Unsatisfactory.csv)
"""

df4=df3[(df3["CodeKata Score"]>15000)]
print("\nNo. of rows and columns",df4.shape[0],end="\n\n")
df4.to_csv('Exceeded expectations.csv')
print("\nExceeded expectations.csv is created\n")
df4

df5=df3[(df3["CodeKata Score"]<15000)&(df3["CodeKata Score"]>10000)]
print("No. of rows and columns",df5.shape[0],end="\n\n")
df5.to_csv('Reached_expectations.csv')
print("\nReached_expectations.csv is created\n")
df5

df6=df3[(df3["CodeKata Score"]>7000)&(df3["CodeKata Score"]<10000)]
print("No. of rows and columns",df6.shape[0],end="\n\n")
df6.to_csv('Needs_Improvement.csv')
print("\nNeeds_Improvement.csv is created\n")
df6

df7=df3[(df3["CodeKata Score"]<7000)]
print("No. of rows and columns",df7.shape[0],end="\n\n")
df7.to_csv('Unsatisfactory.csv')
print("\nUnsatisfactory.csv is created\n")
df7

print("\nThe total no. of rows in merged CSVs (college_1.csv and college_2.csv): {}".format(df3.shape[0]))

x=[df4,df5,df6,df7]
print("\nThe total no. of rows in merged CSVs (Exceeded expectations.csv, Reached_expectations.csv, Needs_Improvement.csv, Unsatisfactory.csv): {}".format(pd.concat(x).shape[0]))

"""###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)"""

print("Average of Previous Geekions is {}".format(df3["Previous Geekions"].mean()))

print("Average of Average of CodeKata Score is {}".format(df3["CodeKata Score"].mean()))

print("\n Average of Previous Geekions vs CodeKata Score\n")
m=px.scatter(df3,x="Previous Geekions",y='CodeKata Score',color="Rising")
m.update_layout(
    title="Average of Previous Geekions vs CodeKata Score",
    xaxis_title="Index",
    yaxis_title="Previous Geekions",
)
m.show()

"""###### No of students participated """

df3["Name"] = df3["Name"].str.lower() 
df3["Name"] = df3["Name"].str.strip()
df3["Name"].isnull().sum()

print("\nTotal no. of student participated is {}".format(df3["Name"].nunique()))

"""###### #Average completion of python course or my_sql or python english or computational thinking"""

x=['python','mysql','python_en','computational_thinking']

for i in x:
  print("\nThe average of the {} is {}".format(i,df3[i].mean()))

"""###### rising star of the week (top 3 candidate who performed well in that particular week)"""

df3.Rising.unique()

df3.Rising.nlargest(3)

q=list(df3.sort_values(by=["Rising"],ascending=[False])["Name"].head(3))
r=list(df3.sort_values(by=["Rising"],ascending=[False])["Rising"].head(3))
print("\nTop 3 rising star of the week \n")
print(*q, sep = "\n")

print("\nrising star of the week\n")
m1=px.bar(x=r,y=q, color=q, orientation='h')
m1.update_layout(
    title="rising star of the week",
    xaxis_title="Rising point",
    yaxis_title="Name",
)
m1.show()

"""###### Shining stars of the week (top 3 candidates who has highest geekions)"""

print("\nShining stars of the week\n")
t=px.scatter(df3,x="Previous Geekions",size="Previous Geekions",color='Previous Geekions',hover_name='Name')
t.update_layout(
    title="Shining stars of the week",
    xaxis_title="Index",
    yaxis_title="Previous Geekions",
)
t.show()

w=list(df3.sort_values(by=["Previous Geekions"],ascending=[False])["Name"].head(3))
print("\nTop 3 rising star of the week \n")
print(*w, sep = "\n")

"""###### Department wise codekata performence (pie chart)"""

w=list(df3["Department"].unique())
w

df3.groupby("Department")["CodeKata Score"].sum()

plt.pie(df3.groupby("Department")["CodeKata Score"].sum(), labels = w, autopct='%1.0f%%', data=True)
print("\nDepartment wise codekata performence\n")
plt.show()

"""###### Department wise toppers (horizantal bar graph or any visual representations of your choice)"""

print("\nDepartment codekata score and name\n")
t1=px.scatter(df3,x="Department",y='CodeKata Score',size='CodeKata Score',color='Name',title="Department wise Topper")
t1.update_layout(
    title="Department wise codekata score and name"
)
t1.show()

toppername=[]

x1=df3[df3["Department"]=="Computer Science and Engineering"]
mcs=x1["CodeKata Score"].max()
toppername.append(x1.Name[x1["CodeKata Score"]==x1["CodeKata Score"].max()].values[0])
x2=df3[df3["Department"]=="Electronics and Communication Engineering"]
me=x2["CodeKata Score"].max()
toppername.append(x2.Name[x2["CodeKata Score"]==x2["CodeKata Score"].max()].values[0])
x3=df3[df3["Department"]=="Electronics and Electrical Engineering"]
mee=x3["CodeKata Score"].max()
toppername.append(x3.Name[x3["CodeKata Score"]==x3["CodeKata Score"].max()].values[0])

print(toppername)

z1=["Computer Science","Electronics and Communication Engineering","Electronics and Electrical Engineering"]
z2=[mcs,me,mee]
print("\nDepartment wise toppers names")
fig=px.bar(x=z1,y=z2, color=toppername,title="Department wise Topper")
fig.update_layout(
    title="Department wise toppers names"
)
fig.show()