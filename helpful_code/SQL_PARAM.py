#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import Tk
r = Tk()
r.withdraw()

param = input('Enter Query Parameter')

count = len(param.split())
output = []
for x in param.split():
    if count>1:
        output.append("'" + x + "'" + ",")
    else:
        output.append("'" + x + "'")
    count-=1


# In[4]:


r.clipboard_append(output)


# In[5]:


r.update()

