#!/usr/bin/env python
# coding: utf-8

# In[ ]:


total = 0.0

for n in range(1,1000000001):
    total = total + (((-1)**(n+1))*4.0)/(2.0 * n - 1)
    
    if (n % 1000000 == 0):
        print (f'Total = {total}')


# In[ ]:




