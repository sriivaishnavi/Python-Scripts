#!/usr/bin/env python
# coding: utf-8

# In[9]:


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[10]:


fromaddr = "sriiivaishnavi@gmail.com"
toaddr = "sriivaishnavi@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"


# In[11]:


body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))


# In[12]:


import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("sriiivaishnavi@gmail.com", "Sriv@ishnavi5")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)


# In[ ]:




