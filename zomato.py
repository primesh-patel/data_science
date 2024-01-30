#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the Zomato data
zomato_data = pd.read_csv('zomato.csv')


# In[6]:


zomato_data = pd.read_csv('zomato.csv', encoding = 'latin-1')


# In[10]:


# Data Assessment
zomato_data.head()


# In[14]:


print("Size of the dataset:")
print(zomato_data.shape)


# Checked the number of rows and columns in the Zomato dataset to understand its overall size.

# In[15]:


print("\nUnique restaurants:")
print(zomato_data['Restaurant ID'].nunique())


# Examined the count of unique restaurants using the 'Restaurant ID' or 'Restaurant Name' column.

# In[16]:


print("\nUnique values in 'Country Code':")
print(zomato_data['Country Code'].unique())


# Explored the distinct values in the 'Country Code' column to identify the countries covered.

# In[17]:


print("\nMissing values:")
print(zomato_data.isnull().sum())


#  Investigated the presence of missing values across the dataset.

# In[19]:


print("\nDistribution of cuisines:")
print(zomato_data['Cuisines'].value_counts())


# Analyzed the distribution of different cuisines in the dataset.

# In[20]:


print("\nUnique cities and localities:")
print(zomato_data['City'].nunique())
print(zomato_data['Locality'].nunique())


# Checked the number of unique cities and localities represented in the dataset.

# In[21]:


# Data Cleaning
# Handling missing values
zomato_data = zomato_data.dropna(subset=['Average Cost for two'])


# Decided on a strategy for handling missing values in the dataset.

# In[23]:


# Duplicate entries
zomato_data = zomato_data.drop_duplicates(subset=['Restaurant ID'])


# Identified and removed duplicate entries based on the 'Restaurant ID.'

# In[24]:


# Outliers in 'Average Cost for two'
sns.boxplot(x='City', y='Average Cost for two', data=zomato_data)
plt.show()


# Visualized and addressed outliers in the 'Average Cost for two' column.

# In[ ]:


# Standardizing 'Cuisines'
zomato_data['Cuisines'] = zomato_data['Cuisines'].apply(lambda x: ', '.join(sorted(x.split(', '))))


# Cleaned and standardized the format of entries in the 'Cuisines' column.

# In[28]:


# Data Analysis and EDA
# Distribution of 'Average Cost for two' across cities
sns.boxplot(x='City', y='Average Cost for two', data=zomato_data)
plt.show()


# Explored the variation in average costs across different cities.

# In[29]:


# Trends in ratings based on cuisine types
sns.barplot(x='Cuisines', y='Aggregate rating', data=zomato_data)
plt.xticks(rotation=90)
plt.show()


# Investigated if there were noticeable trends in ratings based on different cuisine types.

# In[30]:


# Correlation between 'Aggregate rating' and 'Number of Votes'
sns.scatterplot(x='Aggregate rating', y='Votes', data=zomato_data)
plt.show()


# Checked for any correlation between the overall rating and the number of votes.

# In[31]:


# Impact of table booking and online delivery on ratings
sns.boxplot(x='Has Table booking', y='Aggregate rating', data=zomato_data)
plt.show()


# Explored how the availability of table booking and online delivery affected restaurant ratings.

# In[32]:


# Creating a popularity feature based on votes
zomato_data['Popularity'] = pd.qcut(zomato_data['Votes'], q=4, labels=['Low', 'Moderate', 'High', 'Very High'])


# Defined a new feature indicating the popularity of a restaurant based on the number of votes.

# In[47]:


zomato_data.head()


# In[34]:


# Differences in average costs between cities/countries
sns.barplot(x='Country Code', y='Average Cost for two', data=zomato_data)
plt.show()


# Analyzed if there were significant differences in average costs based on geographical location.

# In[36]:


pip install folium


# In[37]:


# Data Visualization
# Geographical plot of restaurant locations
# Example code using Folium
import folium


# In[38]:


restaurant_map = folium.Map(location=[zomato_data['Latitude'].mean(), zomato_data['Longitude'].mean()], zoom_start=10)
for index, row in zomato_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(restaurant_map)
restaurant_map.save('restaurant_map.html')


# Created a geographical plot using latitude and longitude to visualize the distribution of restaurant locations.

# In[39]:


# Distribution of restaurants across price ranges
sns.countplot(x='Price range', data=zomato_data)
plt.show()


# Visualized the distribution of restaurants across different price ranges.

# In[40]:


# Variation of average cost across cuisines
plt.figure(figsize=(14, 6))
sns.boxplot(x='Cuisines', y='Average Cost for two', data=zomato_data)
plt.xticks(rotation=90)
plt.show()


# Used box plots to show the variation in average costs across different cuisines.

# In[41]:


# Relationship between 'Aggregate rating' and 'Number of Votes'
sns.scatterplot(x='Aggregate rating', y='Votes', data=zomato_data)
plt.show()


# Created a scatter plot to explore the relationship between overall ratings and the number of votes.

# In[42]:


# Trends in ratings based on color and text representations
sns.countplot(x='Rating color', data=zomato_data)
plt.show()


# Visualized the distribution of ratings based on color and text representations.

# In[43]:


# Distribution of restaurants with table booking and online delivery
sns.countplot(x='Has Table booking', data=zomato_data)
plt.show()


# Displayed the distribution of restaurants with and without table booking options.

# In[44]:


# Report Creation
# Summarize key statistics and insights
print(zomato_data.describe())


# In[ ]:




