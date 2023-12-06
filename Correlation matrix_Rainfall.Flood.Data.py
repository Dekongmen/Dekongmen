#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[7]:


df = pd.read_csv('D:/Upper West Flood Risks_Manuscript/Datasets/NADMO UWR/Correlation/RainFloodData.csv')


# In[8]:


df.head()


# In[16]:


df.tail()


# In[17]:


corr=df.corr()
corr


# In[23]:


plt.figure(figsize=(5,5))
sns.heatmap(corr,square=True, cmap='crest', linewidths=1, annot=True) #vmin=-1, vmax=1,
plt.show()


# In[24]:


matrix=np.triu(corr)
matrix


# In[25]:


plt.figure(figsize=(8,8))
sns.heatmap(corr, mask=matrix, square=True, cmap='bwr',  linewidths=0.5, annot=True)
plt.show()


# In[ ]:




