#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv('mtcars.csv')

plt.hist(df['mpg'], bins=10, edgecolor='black')

plt.title('Frequency Distribution of MPG')
plt.xlabel('Miles Per Gallon (MPG)')
plt.ylabel('Frequency')

plt.show()

hist, bin_edges = np.histogram(df['mpg'], bins=10)
interval_with_highest_frequency = (bin_edges[hist.argmax()], bin_edges[hist.argmax() + 1])

interval_with_highest_frequency


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')

plt.scatter(df['wt'], df['mpg'], color='blue')

plt.title('Relationship Between Car Weight and MPG')
plt.xlabel('Weight of the Car (1000 lbs)')
plt.ylabel('Miles Per Gallon (MPG)')

plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')

plt.bar(transmission_counts.index, transmission_counts.values, color=['blue', 'orange'])

plt.title('Frequency Distribution of Transmission Types')
plt.xlabel('Transmission Type')
plt.ylabel('Number of Cars')

plt.show()


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')

plt.boxplot(df['mpg'], vert=False, patch_artist=True)

plt.title('Box Plot of MPG')
plt.xlabel('Miles Per Gallon (MPG)')

plt.show()

five_number_summary = df['mpg'].describe()[['min', '25%', '50%', '75%', 'max']]
five_number_summary


# In[22]:


import numpy as np 
import pandas as pd


# In[25]:


import pandas as pd
import numpy as np
df = pd.read_csv('rainfall in india 1901-2015.csv')
df


# In[26]:


df.info()


# In[28]:


sorted_df = df.sort_values(by = 'ANNUAL', ascending=False)
highest = sorted_df.iloc[0,1]
print("District that gets the highest annual rainfall:",highest)


# In[30]:


new_df = df.drop(['JAN','FEB', 'MAR','JUN', 'JUL','SEP', 'OCT','DEC'],axis=1)
new_df


# In[ ]:





# In[ ]:




