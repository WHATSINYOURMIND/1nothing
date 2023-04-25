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
print("original columns: ")
print(df)
print("New column : Colour ")
colour = ['red', 'blue', 'purple', 'orange', 'black'] #syntax for adding new column
df['colour'] = colour
print("updated column : ")
print(df)


         
