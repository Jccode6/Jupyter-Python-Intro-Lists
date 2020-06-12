"""
I'm trying to create a dataframe with the columns
Name, City, Age, and Scores and create an index column
using the row_labels variable
"""


import pandas as pd
import numpy as np

data = { 'Name': ['Joseph', 'Todd', 'Michelle', 'Shaquan','Nicky','Brittany', 'James', 'Sharon', 'Janel',
                  'Tyrone', 'Jameisha', 'Jarod', 'Cedric', 'Jada', 'Dorone', 'Andrew', 'Charity', 'Brad'
                  'Jadon', 'Michaela' 'Jordan', 'Santiago', 'Rachel', 'Lee', 'Joellen', 'Eden', 'Adam'],
         'City': ['Dallas', 'Orlando', 'Miami', 'Washington DC', 'Detroit', 'Atlanta', 'New York',
                  'Seattle', 'San Francisco', 'Dallas', 'Phoenix', 'Orlando', 'Atlanta', 'Jacksonville',
                  'Houston', 'Los Angeles' 'Chicago', 'Miami', 'Dallas', 'New Orleans', 'Chicago', 'New York',
                  'Orlando', 'San Jose', 'San Francisco', 'Chicago', 'Washington DC'],
         'Age' : [34, 29, 24, 31, 33, 28, 35, 32, 28, 24, 40, 37, 30, 27, 32, 35, 29,
                  39, 34, 24, 33, 25, 23, 31, 28, 36, 23],
         'Scores' : [98.0, 87.0, 90.0, 85.0, 94.0, 83.0, 87.0, 80.0, 95.0, 78.0,
                     90.0, 85.0, 77.0, 91.0, 78.0, 88.0, 85.0, 80.0, 99.0, 93.0,
                     84.0, 84.0, 88.0, 98.0, 95.0, 91.0, 94.0]

}

row_labels = list(np.arange(101, 126, 1))

df = pd.DataFrame(data=data, index=row_labels)
df
