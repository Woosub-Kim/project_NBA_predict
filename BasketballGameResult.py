#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#승패
def result_fnc0(difference):
    if difference > 0:
        return 'home'
    elif difference < 0:
        return  'away'