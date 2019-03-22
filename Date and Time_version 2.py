#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[2]:


now = datetime.datetime.now()


# In[3]:


print(now)


# In[5]:


print(now.year)


# In[6]:


print(now.month)


# In[7]:


print(now. day)


# In[9]:


print(now.hour)


# In[10]:


print(now.second)


# In[11]:


print(now.minute)


# In[12]:


print(now.microsecond)


# In[13]:


#print date and time 1 week ago
print("1 week ago it is", now - datetime.timedelta(weeks=1))


# In[14]:


#print 100 days ago
print("100 days ago",now-datetime.timedelta(days=100))


# In[16]:


#print 1 week from now
print("1 week from now it was", now+datetime.timedelta(weeks=1))


# In[18]:


#print 1000 days from now
print("1000 days from now", now + datetime.timedelta(days=1000))


# In[19]:


birthday = datetime.datetime(1994,9,5)


# In[24]:


print("Age calculation in days",now-birthday)


# In[ ]:




