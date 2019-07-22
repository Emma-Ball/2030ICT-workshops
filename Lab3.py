#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import numpy as np
x = np.linspace(0,5,11)
y = x ** 2


# In[6]:


x


# In[7]:


y


# In[8]:


plt.plot(x,y,'r') # ;'r' is the colour red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show


# In[13]:


# plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x,y,'r--') # more on colour options later
plt.subplot(1,2,2)
plt.plot(y,x,'g*-');


# In[14]:


# Create figure (empty canvas)
fig = plt.figure()

# Add set of axes to figure
axes = fig.add_axes([0.1,0.1,0.8,0.8]) # left, bottom, width, height

# Plot on that set of axes
axes.plot(x,y,'b')
axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('Set Y Label')
axes.set_title('Set Title')


# In[15]:


#creates a blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) # the main axes
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # the inset axes

# Larger Figure Axes 1
axes1.plot(x,y,'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y,x,'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')


# In[16]:


#use similar to plt.figure() except use tuple unpacking to grap fig and axes
fig, axes = plt.subplots()

# Now use the axes object to add stuff to plot
axes.plot(x,y,'r')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')


# In[18]:


# Empty canvas of 1 by 2 subplots 
fig, axes = plt.subplots(nrows=1, ncols=2)


# In[19]:


# Axes is an array of axes to plot on 
axes


# In[20]:


for ax in axes:
    ax.plot(x,y,'b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Title')
# Display the figure object
fig


# In[21]:


fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x,y,'g')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Title')

fig
plt.tight_layout()


# In[22]:


fig = plt.figure(figsize=(8,4), dpi=100)


# In[23]:


fig, axes = plt.subplots(figsize=(12,3))
axes.plot(x,y,'r')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title');


# In[24]:


fig.savefig("filename.png")


# In[25]:


fig.savefig("filename.png", dpi=200)


# In[26]:


ax.set_title("title");


# In[28]:


ax.set_xlabel("x")
ax.set_ylabel("y");


# In[29]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()


# In[33]:


fig, axes = plt.subplots(1,3,figsize=(12,4))

axes[0].plot(x, x**2, label="x**2")
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3, label="x**3")
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3, label="x**3")
axes[2].set_ylim([0,60])
axes[2].set_xlim([2,5])
axes[2].set_title("custom axes range")


# In[34]:


plt.scatter(x,y)


# In[36]:


from random import sample
data = sample(range(1,1000),100)
plt.hist(data)


# In[38]:


data = [np.random.normal(0, std, 100) for std in range(1,4)]

#rectangular box plot
plt.boxplot(data,vert=True, patch_artist=True);


# In[40]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[43]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlim([0, 100])
ax.set_ylim([0,200])
ax.set_title('title')


# In[113]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax2.set_xticks([0.0,0.2,0.4, 0.6,0.8,1.0])
ax2.set_yticks([0.0,0.2,0.4, 0.6,0.8,1.0])


# In[112]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])

ax1.plot(x,y, 'r')
ax1.set_xlim(0,100)
ax1.set_ylim(0,200)
ax2.plot(x,y, 'r')
ax2.set_xlim(0,100)
ax2.set_ylim(0,200)
ax2.set_xticks([0,20,40, 60,80,100])
ax2.set_yticks([0,50,100,150,200])


# In[51]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])


# In[105]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])

ax1.plot(x, z)
ax1.set_xlim(0,100)
ax1.set_ylim(0,10000)
ax2.plot(x,y)
ax2.set_xlim(20.0,22.0)
ax2.set_ylim(30,50)

ax2.set_title('zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')


# In[69]:


plt.subplots(nrows=1, ncols=2)


# In[125]:


fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y, lw=3, ls="--", color="blue")
axes[0].set_xlim(0, 100)
axes[0].set_ylim(0, 200)
axes[1].plot(x,z, "r", lw=3)
axes[1].set_xlim(0, 100)
axes[1].set_ylim(0, 10000)


# In[127]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,3))
axes[0].plot(x,y, lw=3)
axes[0].set_xlim(0, 100)
axes[0].set_ylim(0, 200)
axes[1].plot(x, z, "r--", lw=3)
axes[1].set_xlim(0, 100)
axes[1].set_ylim(0, 10000)


# In[ ]:




