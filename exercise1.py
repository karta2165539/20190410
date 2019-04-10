
# coding: utf-8

# In[1]:

print("hi")


# In[2]:

import requests


# In[5]:

response=requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")


# In[6]:

response.encoding="big5"


# In[7]:

book1=response.text


# In[8]:

book1[:]


# In[11]:

book1[:50]


# In[12]:

book1[800:900]


# In[13]:

book1[100:200:2]


# In[14]:

book1[0:10:2]


# In[15]:

book1[:100:10]


# In[16]:

book1[300::50]


# In[17]:

book1[::20]


# In[ ]:



