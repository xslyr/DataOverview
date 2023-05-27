# DataOverview
Library with functionalities similar a "Pandas Dataframe Describe".

Current methods:
  - details: this variable will return you some dataframe describe of all columns with a aditional data like mode, null count, etc.
  - columns_type(): return a dictionary that show you a column types distribution.
  - show(): this method will filter details variable showing you only columns by type.
      parameter: type: can be one of follows ['all','int64','float64','object','bool', 'datetime64']

Usage:

import pandas as pd
import dfview as ovw  #import a library

df = pd.read_csv('my_data.csv')

# init our object
describe = ovw.DataOverview(df)

# showing only int columns 
describe.show(type='int64')

# showing only string columns 
describe.show(type='object')

...
