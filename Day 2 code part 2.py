#!/usr/bin/env python
# coding: utf-8

# In[1]:


A=[1,2,3,4,5]
A.append(5)
A


# In[2]:


A.append(6,7)
A


# In[3]:


A.append([6,7,8,9])
A


# In[4]:


B=[1,2]
B
B.clear()
B


# In[8]:


del B
B


# In[9]:


A


# In[10]:


A.append(("DHANUSH",2004,1,6))
A


# In[11]:


len(A)


# In[12]:


A[6][1]


# In[13]:


B=A.copy()
B


# In[14]:


C=A
C


# In[15]:


C.count(5)


# In[16]:


C.index(1)


# In[17]:


C.index(5)


# In[19]:


C.pop()


# In[20]:


C


# In[21]:


C.remove(5)
C


# In[23]:


C.reverse()
C


# In[25]:


A.reverse()
A


# In[26]:


D=[1,2,3,4]
D
D.reverse()
D


# In[27]:


D.sort()


# In[29]:


D.append("DHANUSH")
D


# In[30]:


D.sort()


# In[31]:


S=[1,2245,2,6,86,56]
S.sort()
S


# In[32]:


S.sort(reverse=True)
S


# In[33]:


S.insert(0,"DHANUSH")
S


# In[34]:


S.extend([2,66,55])
S


# In[36]:


S.extend(["DHANUSH"])
print(S)


# In[44]:


F=["DHANUSH","ABI"]
F
F.extend('DHANUSH')
F


# In[ ]:




