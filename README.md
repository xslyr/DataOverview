# DataOverview
Library with goals similar to "Pandas Dataframe Describe".

Current functions:
   - details: this variable will return you some dataframe describe of all columns with an additional data like mode, null count, etc.
   - columns_type(): return a dictionary that show you a column types distribution.
   - show(): this method will filter details variable showing you only columns by type.
       parameter: type: can be one of follows 'all','int64','float64','object','bool', 'datetime64'.

Usage:

```
import pandas as pd
import dfview as ovw  

df = pd.read_csv("my_data.csv")
describe = ovw.DataOverview(df)

# getting dictionary of type columns distribuction
cols = describe.columns_type()
print(cols)

# showing describe by type of columns
describe.show(type="int64")
describe.show(type="object")

```



