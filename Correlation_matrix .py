#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[39]:


df = pd.read_csv('D:/Upper West Flood Risks_Manuscript/Datasets/NADMO UWR/Correlation/FlooddisasterData1.csv')


# In[40]:


df.head()


# In[41]:


corr=df.corr()
corr


# In[43]:


#df1 = df.iloc[0:5,1:4]
#df1


# In[44]:


corr = df.corr()
corr


# In[45]:


plt.figure(figsize=(5,5))
sns.heatmap(corr,square=True, cmap='crest', linewidths=0.1, annot=True) #vmin=-1, vmax=1,
plt.show()


# In[46]:


matrix=np.triu(corr)
matrix


# In[47]:


plt.figure(figsize=(8,8))
sns.heatmap(corr, mask=matrix, square=True, cmap='bwr',  linewidths=0.5, annot=True)
plt.show()


# In[ ]:




