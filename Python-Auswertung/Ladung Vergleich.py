#!/usr/bin/env python
# coding: utf-8

# In[10]:



import matplotlib.pyplot as plt

# x axis values
x1 = [6,16.5,25.5,31.5,37.5,41,55,71,79.5,88.5,94,96.5,97.5,99]
# corresponding y axis values
y1 = [1.6,1.18,1.25,1.4,1.25,1,1.08,0.86,0.61,0.50,0.31,0.14,0.11,0.15]
# x axis values
x2 = [12,34.5,52,67.5,81.5,86.5,91.5,96.5,99]
# corresponding y axis values
y2 = [1.82,0.96,0.71,0.75,0.64,0.5,0.37,0.18,0.09]

# plotting the points
plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12, label="Langsamladung")
 
# plotting the points
plt.plot(x2, y2, color='black', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='orange', markersize=12, label="Schnellladung")

# setting x and y axis range
plt.ylim(0,2)
plt.xlim(0,110)

plt.legend(loc='upper right')
 
# naming the x axis
plt.xlabel('Akkuladung in %')
# naming the y axis
plt.ylabel('dL/dt in %/min')
 
# giving a title to my graph
plt.title('Ladekurve differenziell, iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[11]:


import matplotlib.pyplot as plt
 
# x axis values
x1 = [0,5,16,20,25,29,31,53,60,78,92,107,114,123,138]
# corresponding y axis values
y1 = [2,10,23,28,35,40,42,68,74,85,92,96,97,98,100]
# x axis values
x2 = [0,11,27,31,59,70,76,95,112,135]
# corresponding y axis values
y2 = [2,22,47,57,78,85,88,95,98,100]
 
# plotting the points
plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12, label="Langsamladung")
plt.plot(x2, y2, color='black', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='orange', markersize=12, label="Schnellladung") 




# setting x and y axis range
plt.ylim(0,110)
plt.xlim(0,140)

plt.legend(loc='lower right')
 
# naming the x axis
plt.xlabel('Zeit in min')
# naming the y axis
plt.ylabel('Ladung in %')
 
# giving a title to my graph
plt.title('Ladekurve absolut, iPhone XS Max (Batteriezustand 96%)')
 
# function to show the plot
plt.show()


# In[ ]:




