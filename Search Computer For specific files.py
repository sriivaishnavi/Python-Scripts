#!/usr/bin/env python
# coding: utf-8

# In[10]:


#using fnmatch & os.walk to search image fiels in computer
import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirs, files in os.walk("C:\Program Files"):
    for extensions in images:
        for filename in fnmatch.filter(files, extensions):
            matches.append(os.path.join(root, filename))

print(matches)


# In[ ]:




