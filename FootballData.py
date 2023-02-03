#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
data_frame = pd.read_csv('data.csv')
data_frame.shape


# In[4]:


data_frame.describe()


# In[5]:


data_frame.values


# In[6]:


df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value'])
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', ''))*1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', ''))*1000000
        return 1000000.0
    if 'B' in x:
        if len(x) > 1:
            return float(x.replace('B', ''))*1000000000
        return 0.0
        
wage = df1['Wage'].replace('[\€]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value'] = value

df1['difference']=df1['Value']-df1['Wage']
df1.sort_values('difference', ascending=False)


# In[7]:


import seaborn as sns
sns.set()

graph = sns.scatterplot(x='Wage', y='Value', data=df1)
graph


# In[8]:


from bokeh.plotting import figure,show
from bokeh.models import HoverTool

hover = HoverTool(tooltips=[])

p = figure(title='Fifa 2019', x_axis_label='Wage', y_axis_label='Value', plot_width=700, plot_height=700, tools=[])
p.circle('Wage', 'Value', size=10, source=df1)
show(p)


# In[ ]:




