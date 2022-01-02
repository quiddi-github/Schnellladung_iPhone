#!/usr/bin/env python
# coding: utf-8

# In[10]:



import matplotlib.pyplot as plt
 
# x axis values
x = [12,34.5,52,67.5,81.5,86.5,91.5,96.5,99]
# corresponding y axis values
y = [1.82,0.96,0.71,0.75,0.64,0.5,0.37,0.18,0.09]
 
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
plt.title('Ladekurve differenziell, Schnellladung iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[11]:


import matplotlib.pyplot as plt
 
# x axis values
x = [0,11,27,31,59,70,76,95,112,135]
# corresponding y axis values
y = [2,22,47,57,78,85,88,95,98,100]
 
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
plt.title('Ladekurve absolut, Schnellladung iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[ ]:




