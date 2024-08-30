#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('data1')


# In[2]:


#1. Calculate and visually represent the overall churn rate
churn_rate = data['Churn'].value_counts(normalize=True) * 100
plt.figure(figsize=(6, 6))
churn_rate.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
plt.title('Overall Churn Rate')
plt.ylabel('')  # Hide the y-label
plt.show()


# In[3]:


# 2. Explore customer distribution by gender, partner status, and dependent status
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# Gender distribution
sns.countplot(x='gender', data=data, ax=ax[0], palette='Set2')
ax[0].set_title('Customer Distribution by Gender')

# Partner status distribution
sns.countplot(x='Partner', data=data, ax=ax[1], palette='Set2')
ax[1].set_title('Customer Distribution by Partner Status')

# Dependent status distribution
sns.countplot(x='Dependents', data=data, ax=ax[2], palette='Set2')
ax[2].set_title('Customer Distribution by Dependent Status')

plt.tight_layout()
plt.show()


# In[4]:


#3. Analyze tenure distribution and its relation with churn
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='tenure', hue='Churn', multiple='stack', palette='Set1')
plt.title('Tenure Distribution and Churn')
plt.xlabel('Tenure (Months)')
plt.ylabel('Number of Customers')
plt.show()


# In[5]:


#4. Investigate churn across different contract types and payment methods
fig, ax = plt.subplots(1, 2, figsize=(18, 6))

# Churn by Contract Type
sns.countplot(x='Contract', hue='Churn', data=data, ax=ax[0], palette='Set1')
ax[0].set_title('Churn by Contract Type')

# Churn by Payment Method
sns.countplot(x='PaymentMethod', hue='Churn', data=data, ax=ax[1], palette='Set1')
ax[1].set_title('Churn by Payment Method')

plt.tight_layout()
plt.show()


# In[ ]:




