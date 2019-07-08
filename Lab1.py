#!/usr/bin/env python
# coding: utf-8

# In[7]:


7**4


# In[8]:


s = "Hi there Sam!"


# In[10]:


s.split()


# In[11]:


planet = "Earth"
diameter = 12742


# In[13]:


print('The diameter of {} is {} kilometers.'.format(planet,diameter))


# In[14]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[15]:


lst[3][1][2][0]


# In[17]:


d = {'kl':[1,2,3,{'tricky':['oh','man','inception', {'target':[1,2,3,'hello']}]}]}


# In[30]:


print(d["kl"][3]["tricky"][3]["target"][3])


# In[31]:


# Tuple is immutable


# In[32]:


def domainGet(param1):
    print(param1.split('@')[1])


# In[34]:


domainGet('user@domain.com')


# In[43]:


def findDog(param1):
    print('dog' in param1.lower().split())


# In[47]:


findDog("Is there a dog here?")


# In[61]:


def countDog(param1):
    lst = param1.lower().split()
    count = 0
    for itm in lst:
     if itm == 'dog':
      count = count+1
    print(count)


# In[65]:


countDog('This dog runs faster than the other dog dude!')


# In[73]:


seq = ['soup', 'dog', 'salad', 'cat', 'great']


# In[75]:


list(filter(lambda item: item[0] == 's', seq))


# In[78]:


def caught_speeding(speed, is_birthday):
    if speed <= 60 or (speed <= 65 and is_birthday == True):
        print("No Ticket")
    elif speed <= 80 or (speed <= 85 and is_birthday == True):
        print("Small Ticket")
    else:
        print("Big Ticket")


# In[88]:


caught_speeding(81, True)


# In[87]:


caught_speeding(81,False)


# In[ ]:




