#!/usr/bin/env python
# coding: utf-8

# In[10]:



import matplotlib.pyplot as plt

# x axis values
x = [6,16.5,25.5,31.5,37.5,41,55,71,79.5,88.5,94,96.5,97.5,99]
# corresponding y axis values
y = [1.6,1.18,1.25,1.4,1.25,1,1.08,0.86,0.61,0.50,0.31,0.14,0.11,0.15]
 
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
# setting x and y axis range
plt.ylim(0,2)
plt.xlim(0,110)
 
# naming the x axis
plt.xlabel('Akkuladung in %')
# naming the y axis
plt.ylabel('dL/dt in %/min')
 
# giving a title to my graph
plt.title('Ladekurve differenziell, Langsamladung iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[11]:


import matplotlib.pyplot as plt
 
# x axis values
x = [0,5,16,20,25,29,31,53,60,78,92,107,114,123,138]
# corresponding y axis values
y = [2,10,23,28,35,40,42,68,74,85,92,96,97,98,100]
 
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
# setting x and y axis range
plt.ylim(0,110)
plt.xlim(0,140)
 
# naming the x axis
plt.xlabel('Zeit in min')
# naming the y axis
plt.ylabel('Ladung in %')
 
# giving a title to my graph
plt.title('Ladekurve absolut, Langsamladung iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[ ]:




