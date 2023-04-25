import pandas as pd
import numpy as np 

exam_data = {
    'name': ['Sarah','Altaf', 'Jeevika', 'Pranil', 'Pratham'],
    'score': [84, 94, 89, 83, 86],
    'attempts': [2, 1, 1, 1, 1],
    'qualify': ['yes','yes','yes','yes','yes']
}


df=pd.DataFrame(exam_data)
print(df)
df._set_value(0,'score',90) #Syntax to change the value of a column using index
print("Updated score of Sarah ")
print(df)     




         
