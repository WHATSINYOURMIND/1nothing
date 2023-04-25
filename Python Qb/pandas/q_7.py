import pandas as pd
import numpy as np 

exam_data = {
    'name': ['Sarah','Altaf', 'Jeevika', 'Pranil', 'Pratham'],
    'score': [84, 94, 89, 83, 86],
    'attempts': [2, 1, 1, 1, 1],
    'qualify': ['yes','yes','yes','yes','yes']
}
labels = ['a','b','c', 'd','e']

df=pd.DataFrame(exam_data, index=labels)
print("original rows: ")
print(df)
print("New row : Aman ")
df.loc['f'] = ['Aman', 99, 1, 'yes'] #syntax for adding new row
print("updated rows : ")
print(df)
print("Delete row score and display new rows:")
df = df.drop('b') #syntax for deleting a row
print(df)
         
