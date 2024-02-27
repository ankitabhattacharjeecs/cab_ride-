#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exploratory Data Ananlysis on cab rides


# In[3]:


#import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt #The datetime module supplies classes for the manipulation of date and time.
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


cab_df=pd.read_csv('/Users/ankitabhattacharjee/Downloads/Cab_Ride.csv',encoding='utf-8')


# In[8]:


#check imported data 
cab_df.head(2)


# In[9]:


#check the number of rows and columns
cab_df.shape


# In[10]:


#check the datatype of the variable
cab_df.dtypes


# In[11]:


#create a function fix data tyoes of data columns
#the strptime() class method takes two arguments
#string(that be converted to date time)and format the code.
# considering the date is in the mm/dd/yyyy format

def convert_time(column_name):
    y=[]
    for x in cab_df[column_name]:
        y.append(dt.datetime.strptime(x, "%m-%d-%Y %H:%M"))
    cab_df[column_name]=y


# In[12]:


#date time formats.
#NOW convert the columns in date and time format
column_date=cab_df[['START_DATE','END_DATE']]
for x in column_date:
    convert_time(x)


# In[13]:


#use info function to check the data type and the mising values
cab_df.info()


# In[14]:


#basic description of data 
#We can use the describe() to get summary statictics
#define include="all" if you want to describe object type variable
cab_df.describe()


# In[15]:


#check for the missing values
missing=cab_df.isnull().sum()
missing


# In[16]:


#calculate the mode
cab_df.mode(axis=0, numeric_only=False, dropna=True)


# In[18]:


#fill missing values by mode
cab_df['PURPOSE'].fillna("Meeting", inplace=True)


# In[20]:


#again check for the missing values
missing=cab_df.isnull().sum()
missing


# In[21]:


#plot number of trip at each category
x=cab_df['CATEGORY'].value_counts().plot(kind='bar')


# In[24]:


#number of trips per month
#extract month from the start date
count=0
mt=[]
while count < len(cab_df):
    mt.append(cab_df['START_DATE'][count].month)
    count=count+1
cab_df['Month']=mt


# In[28]:


#plot number of trips at each month
x=cab_df['Month'].value_counts()
x.plot(kind='bar',figsize=(10,5),color='orange')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Number of trips per month')
plt.show()


# In[29]:


#calculate the duration of each trip in minutes

cab_df['Duration_Minutes']= cab_df['END_DATE']-cab_df['START_DATE']
cab_df['Duration_Minutes']


# In[30]:


cab_df['Duration_Minutes'][0]


# In[31]:


#convert the time format in to minutes
minutes=[]
for x in cab_df['Duration_Minutes']:
    minutes.append(x.seconds/60)
cab_df['Duration_Minutes']=minutes


# In[32]:


plt.hist(cab_df['Duration_Minutes'],bins=10,color='green')
plt.show()


# In[33]:


cab_df['Duration_Minutes'].describe()


# In[34]:


plt.boxplot(cab_df['Duration_Minutes'])
plt.show()


# In[35]:


#see how many trips made by each purpose
purpose_time=cab_df['PURPOSE'].value_counts()
purpose_time.plot(kind='bar',figsize=(10,5),color='green')
plt.show()


# In[ ]:


# calculate trip speed for each driver


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




