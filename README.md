# DataOverview
Library with goal similar to *Pandas Dataframe Describe* with some additional information.

Current functions:
   - ***details***: This variable return a dataframe with all statistic data. Table on chapter 2, show us a better description of all.
   - ***columns_type***: Return a dictionary that show you a column types distribution.
   - ***show***: This method will filter details variable showing you only columns by type.<br/>
       The unique parameter *type* can be one of follows 'all','int64','float64','object','bool', 'datetime64'.
   - ***obj_distrib***: This method will show the data distribution for column of type 'object'.
       The parameter 3 possible parameter will better explained on chapter 3.

---
#### 1 - Usage:
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

# getting obj distribution all columns, axis=1, include_nulls=True 
describe.obj_distrib()

# getting obj distribution with some specific columns, axis=0, include_nulls=False 
describe.obj_distrib( columns_list=['col1', 'col2', 'col3'], axis=0, include_nulls=False )  

```
---

####  2 - Informations Showed by Variable 'details' or Method 'show'
| Column | Description |
| --- | --- |
| `dtype` |  Type of column data.  |
| `count` |  Count of non null occurrences.  |
| `null` |  Count of null occurrences.  |
| `min` |  Smallest value of columns's data. This applies only for int or float column type.  |
| `mean` |  Mean of data. This applies only for int or float column type.  |
| `max` |  Largest value of column's data. This applies only for int or float column type.  |
| `std` |  Standard deviation of data. This applies only for int or float column type. |
| `std%` |  Percentage that represents the size of standard deviation in comparison of data distribution. This applies only for int or float column type.  |
| `25%` |  Quantile 25% like a pandas describe method.  |
| `50%` |  Quantile 50% like a pandas describe method.  |
| `75%` |  Quantile 75% like a pandas describe method.  |
| `mode` |  Mode of the column or occurrence data with the most repetitions. |
| `n_mode` |  Occurrence count of the data mode.  |

---
####  3 - Paramteters of obj_distrib
| Column | Description |
| --- | --- |
| `column_list` | List of columns that you want show data distribuction. Default value show all tables. |
| `include_nulls` | This boolean parameter include or exclude null values on first occurence of dataframe returned. Default value is True.|
| `axis` | This integer parameter change dataframe disposition. The default value 1 returns columns on top, 0 on left side. |

