import  pandas as pd
import numpy as np 
df=pd.DataFrame({'X':(1,2,3),'Y':(4,5,6),'Z':(7,8,'5')})
print(df)

#pandas using index labelled!
import pandas as pd
import numpy as np
exam_data={'Name':['Amisha','Diya','Nidhi','Raju','Tisha'],
           'Score':[50,55,56,57,54],
           'Attempts':[1,3,None,6,7]}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print(df)
#pandas to print first three rows
import pandas as pd
  import numpy as np
exam_data={'Name':['Amisha','Diya','Nidhi','Raju','Tisha'],
          'Score':[50,55,56,57,54],
          'Attempts':[1,3,np.nan,6,7]}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("first three rows are:")
print(df.iloc[:3])
    

#To print greater than X
import pandas as pd
import numpy as np
exam_data={'Name':['Amisha','Diya','Nidhi','Raju','Tisha'],
      'Score':[30,55,36,57,54],
        'Attempts':[1,3,np.nan,6,7]}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("ROWS WHOSE SCORE IS GREATER THAN 50 IS:")
print(df[df['Score'] > 50])

#print to merge two dataframes (left)
import pandas as pd
import numpy as np
data1=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                    'key2':['K0','K1','K0','K1'],
                    'P':['PO','P1','P2','P3'],
                    'Q':['Q0','Q1','Q2','Q3']})
print(data1)
print("\n")
data2=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                    'key2':['K0','K0','K0','K0'],
                    'R':['R0','R1','R2','R3'],
                    'S':['S0','S1','S2','S3']})
print(data2)
print("\n")
merged_data=pd.merge(data1,data2,how='left',on=['key1','key2'])
print(merged_data)
print("\n")
merged_data=pd.merge(data2,data1,how='left',on=['key1','key2'])
print(merged_data)

#print to merge two dataframes(inner)

import pandas as pd
import numpy as np
data1=pd.DataFrame({'Name':['Amisha','Sanjana','Jay','Komal','Kunal'],
                    'Age':[19,23,11,21,13]})
print(data1)
print("\n")
data2=pd.DataFrame({'Name':['Amisha','Komal','Raju','Nidhi'],
                    'roll':[12,25,32,67]})
print(data2)
print("\n")
merged_data=pd.merge(data1,data2,how='inner',on='Name')
print(merged_data)

#to fill the null value
import pandas as pd
data1=pd.DataFrame({'A':[None,1,None],'B':[3,4,5]})
data2=pd.DataFrame({'A':[3,5,7],'B':[7,None,8]})
print(data1)
data1.combine_first(data2)
print(data2)
print(data1.combine_first(data2))

 #multiple join keys
import pandas as pd
import numpy as np
data1=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                    'key2':['K0','K1','K0','K1'],
                    'P':['PO','P1','P2','P3'],
                    'Q':['Q0','Q1','Q2','Q3']})
print(data1)
print("\n")
data2=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                    'key2':['K0','K0','K0','K0'],
                    'R':['R0','R1','R2','R3'],
                    'S':['S0','S1','S2','S3']})
print(data2)
print("\n")
merged_data=pd.merge(data1,data2,on=['key1','key2'])
print(merged_data)
print("\n")
#two merge series!!

import pandas as pd
sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])

print("Original Series:")
print(sr1)
print(sr2)
print("Combine above series to a dataframe:")
ser_df = pd.DataFrame(sr1, sr2).reset_index()
print(ser_df.head())
print("\nUsing pandas concat:")
ser_df = pd.concat([sr1, sr2], axis = 1)
print(ser_df.head())
print("\nUsing pandas DataFrame with a dictionary, gives a specific name to the columns:")
ser_df = pd.DataFrame({"col1":sr1, "col2":sr2})
print(ser_df.head(5))

 #to fill missing value in time seires!
import pandas as pd
import numpy as np
sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
df = pd.DataFrame(sdata)
df.index = pd.util.testing.makeDateIndex()[0:6]
print("Original DataFrame:")
print(df)
print("\nDataFrame after interpolate:")
print(df.interpolate())

#to add prefix and suffix 
import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,67,78,77]})
print("Original DataFrame")
print(df)
print("\nAdd prefix:")
print(df.add_prefix("OO_"))
print("\nAdd suffix:")
print(df.add_suffix("_OYO"))
                                                                                        
#To get a specified row
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("Value of Row1")
print(df.iloc[0])
print("Value of Row4")
print(df.iloc[3])
                                                                                        
# to get a whole row for the value 4
import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame")
print(df)
print('Rows for colum1 value == 4')
print(df.loc[df['col1'] == 4])

# to add a extra column
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthe','Diya','Tisha','Raju'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("Original rows:")
print(df)
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
df['color'] = color
print("\nNew DataFrame after inserting the 'color' column")
print(df)
                                                                                        
  #To add and delete an row
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthe','Diya','Tisha','Raju'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("Original rows:")
print(df)
print("\nAppend a new row:")
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]

print("Print all records after insert a new record:")
print(df)
print("\nDelete the new row and display the original rows:")
df = df.drop('k')
print(df)

#Mean
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthe','Diya','Tisha','Raju'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("\nMean score for each different student in data frame:")
print(df['score'].mean())

#between
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthe','Diya','Tisha','Raju'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(15, 20)])

