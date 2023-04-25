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
print("Attempts of students clearing exams lesser than 2: ")
print(df[df['attempts']>=2])     # Syntax for greater than,lesser than or equals
         
