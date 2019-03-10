#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
print("root prints out directories only from what you specified")
print("dirs prints out sub-directories from root")
print("files prints out all files from root and directories")
print("*" * 20)
for root, dirs, files in os.walk("C:\Program Files"):
    print("root prints out directories only from what you specified")
    print(root)
    print("*" * 20)
    print("dirs prints out sub-directories from root")
    print(dirs)
    print("*" * 20)
    print("files prints out all files from root and directories")
    print(files)
    print("*" * 20)


# In[13]:


print("This is using getsize to see how much every file consumes")
print("---------------")
from os.path import join, getsize
for root, dirs, files in os.walk("C:\Program Files"):
    print(root, "consumes")
    print(sum([getsize(join(root, name)) for name in files]))
    print("bytes in", len(files), "non-directory files")


# In[ ]:


#Retrieve all mp3 files
import fnmatch
import os
 
rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))


# In[ ]:




