#!/usr/bin/env python
# coding: utf-8

# In[31]:


## multiple logistic regression which tell whter a person is facing cancer or not by the tumor size

import numpy
from sklearn import linear_model

#Reshaped for Logistic function.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

#predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([8.46]).reshape(-1,1))
print(predicted)


# In[14]:





# In[15]:





# In[16]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



