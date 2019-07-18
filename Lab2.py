#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
df.head()


# In[5]:


df.head(10)


# In[7]:


df.tail(4)


# In[8]:


df.size


# In[9]:


len(df)


# In[10]:


df.columns


# In[11]:


df['Hired']


# In[12]:


df['Hired'][:5]


# In[13]:


df['Hired'][5]


# In[14]:


df[['Years Experience', 'Hired']]


# In[15]:


df[["Years Experience", "Hired"]][:5]


# In[16]:


df.sort_values(['Years Experience'])


# In[21]:


degree_counts = df['Level of Education'].value_counts()
degree_counts


# In[22]:


degree_counts.plot(kind='bar')


# In[24]:


labels = ['a', 'b', 'c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':30}


# In[25]:


pd.Series(data=my_list)


# In[26]:


pd.Series(data=my_list,index=labels)


# In[28]:


pd.Series(my_list,labels)


# In[29]:


pd.Series(arr)


# In[30]:


pd.Series(arr,labels)


# In[31]:


pd.Series(d)


# In[32]:


pd.Series(data=labels)


# In[33]:


# Even functions (unlikely that you will use this)
pd.Series([sum,print,len])


# In[34]:


ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany', 'USSR', 'Japan'])


# In[35]:


ser1


# In[36]:


ser2 = pd.Series([1,2,3,4], index = ['USA', 'Germany', 'Italy', 'Japan'])


# In[37]:


ser2


# In[38]:


ser1['USA']


# In[39]:


ser1 + ser2


# In[40]:


from numpy.random import randn
np.random.seed(101)


# In[41]:


df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[42]:


df


# In[43]:


df['W']


# In[44]:


# Pass a list of column names
df[['W','Z']]


# In[45]:


# SQL Syntax (NOT RECCOMENDED!)
df.W


# In[46]:


type(df['W'])


# In[47]:


df['new'] = df['W'] + df['Y']


# In[48]:


df


# In[49]:


# Return a new DataFrame with the 'new'
# column dropped
df.drop('new',axis=1)


# In[51]:


# Not inplace unless specified
df


# In[52]:


# Drop the 'new' column of the DataFrame itself
df.drop('new',axis=1,inplace=True)


# In[53]:


df


# In[54]:


df.drop('E', axis=0)


# In[56]:


df.loc['A']


# In[57]:


df.iloc[2]


# In[58]:


df.loc['B','Y']


# In[59]:


df.loc[['A','B'],['W','Y']]


# In[60]:


df


# In[61]:


df>0


# In[62]:


df[df>0]


# In[63]:


df[df['W']>0]


# In[65]:


df[df['W']>0]['Y']


# In[66]:


df[df['W']>0][['Y', 'X']]


# In[67]:


df[(df['W']>0) & (df['Y'] > 1)]


# In[68]:


df


# In[69]:


# Reset tp default 0,1...n index
df.reset_index()


# In[70]:


newind = 'CA NY WY OR CO'.split()


# In[71]:


df['States'] = newind


# In[72]:


df


# In[73]:


df.set_index('States')


# In[74]:


df


# In[75]:


df.set_index('States',inplace=True)


# In[76]:


df


# In[77]:


# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[78]:


hier_index


# In[79]:


df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# In[80]:


df.loc['G1']


# In[81]:


df.loc['G1'].loc[1]


# In[82]:


df.index.names


# In[83]:


df.index.names = ['Group', 'Num']


# In[84]:


df


# In[85]:


df.xs('G1')


# In[86]:


df.xs(['G1',1])


# In[87]:


df.xs(1,level='Num')


# In[90]:


df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[5,np.nan,np.nan],
                   'C':[1,2,3]})


# In[91]:


df


# In[92]:


df.dropna()


# In[94]:


df.dropna(axis=1)


# In[95]:


df.dropna(thresh=2)


# In[96]:


df.fillna(value='FILL VALUE')


# In[97]:


df['A'].fillna(value=df['A'].mean())


# In[102]:


# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[103]:


df = pd.DataFrame(data)


# In[104]:


df


# In[105]:


df.groupby('Company')


# In[106]:


by_comp = df.groupby('Company')


# In[107]:


by_comp.mean()


# In[108]:


df.groupby('Company').mean()


# In[109]:


by_comp.std()


# In[110]:


by_comp.min()


# In[111]:


by_comp.max()


# In[112]:


by_comp.count()


# In[114]:


by_comp.describe()


# In[115]:


by_comp.describe().transpose()


# In[116]:


by_comp.describe().transpose()['GOOG']


# In[118]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0,1,2,3])


# In[119]:


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4,5,6,7])


# In[120]:


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8,9,10,11])


# In[121]:


df1


# In[122]:


df2


# In[123]:


df3


# In[124]:


pd.concat([df1,df2,df3])


# In[126]:


pd.concat([df1,df2,df3],axis=1)


# In[127]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})


# In[128]:


left


# In[129]:


right


# In[130]:


pd.merge(left,right,how="inner",on="key")


# In[136]:


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                          'key2': ['K0', 'K0', 'K0', 'K0'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']})


# In[137]:


pd.merge(left, right, on=['key1', 'key2'])


# In[138]:


pd.merge(left, right, how='outer', on=['key1', 'key2'])


# In[139]:


pd.merge(left, right, how='right', on=['key1', 'key2'])


# In[140]:


pd.merge(left, right, how='left', on=['key1', 'key2'])


# In[146]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2',]},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                         index=['K0', 'K2', 'K3'])


# In[148]:


left.join(right)


# In[149]:


left.join(right, how='outer')


# In[160]:


df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444], 'col3':['abc', 'def', 'ghi', 'xyz']
    })
df.head()


# In[154]:


df['col2'].unique()


# In[155]:


df['col2'].nunique()


# In[158]:


df['col2'].value_counts()


# In[161]:


# Select from DataFrame using criteria from mutiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]


# In[162]:


newdf


# In[163]:


def times2 (x):
    return x*2


# In[164]:


df['col1'].apply(times2)


# In[165]:


df['col3'].apply(len)


# In[166]:


df['col1'].sum()


# In[167]:


del df['col1']


# In[168]:


df


# In[169]:


df.columns


# In[170]:


df.index


# In[171]:


df


# In[174]:


df.sort_values(by='col2') # inplace=False by default


# In[175]:


df.isnull()


# In[176]:


# Drop rows with NaN Values
df.dropna()


# In[3]:


df = pd.DataFrame({'col1':[1,2,3,np.nan],
                  'col2':[np.nan,555,666,444],
                  'col3':['abc','def','ghi','xyz']})
df.head()


# In[4]:


df.isnull()


# In[5]:


df.dropna()


# In[6]:


df.fillna('FILL')


# In[7]:


data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
                     'B': ['one', 'one', 'two', 'two', 'one', 'one'],
                        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
                        'D': [1,3,2,5,4,1,]}
df = pd.DataFrame(data)


# In[8]:


df


# In[9]:


df.pivot_table(values='D',index=['A', 'B'], columns=['C'])


# In[18]:


df = pd.read_csv('example.csv')
df


# In[20]:


df.to_csv('example.csv',index=False)


# In[24]:


pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# In[25]:


df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# In[26]:


from sqlalchemy import create_engine


# In[27]:


engine = create_engine('sqlite:///:memory:')


# In[28]:


df.to_sql('data', engine)


# In[29]:


sql_df = pd.read_sql('data',con=engine)


# In[30]:


sql_df


# In[ ]:




