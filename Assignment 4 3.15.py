#!/usr/bin/env python
# coding: utf-8

# In[10]:


number = 1
e = 0.0
factorial = 1

accuracy = int(input('Enter Accuracy'))

while number < accuracy:
    
    factorial = factorial * number
    
    e = e + 1 / factorial
    number = number + 1

print(f'The value of e is {e+1}')


# In[ ]:





# In[ ]:




