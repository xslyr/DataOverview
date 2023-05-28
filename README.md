# DataOverview
Library with goal similar to *Pandas Dataframe Describe* with some additional information.

Current functions:
   - ***details***: This variable return a dataframe with all statistic data. Table below usage section, show us a better description of all.
   - ***columns_type***: Return a dictionary that show you a column types distribution.
   - ***show***: This method will filter details variable showing you only columns by type.<br/>
       The parameter *type* can be one of follows 'all','int64','float64','object','bool', 'datetime64'.

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

# showing entire describe 
describe.details
describe.show(type='all')

```
---
####  Informations Showed by our Describe

| Column | Description |
| --- | --- |
| `dtype` |  Type of column data.  |
| `count` |  Count of non null occurrences.  |
| `null` |  Count of null occurrences.  |
| `mean` |  Mean of data. This applies only for int or float column type.  |
| `std` |  Standard deviation of data. This applies only for int or float column type. |
| `std%` |  Percentage that represents the size of standard deviation in comparison of data distribution. This applies only for int or float column type.  |
| `min` |  Smallest value of columns's data. This applies only for int or float column type.  |
| `max` |  Largest value of column's data. This applies only for int or float column type.  |
| `mode` |  Mode of the column or occurrence data with the most repetitions. |
| `n_mode` |  Occurrence count of the data mode.  |
| `25%` |  Quantile 25% like a pandas describe method.  |
| `50%` |  Quantile 50% like a pandas describe method.  |
| `75%` |  Quantile 75% like a pandas describe method.  |

