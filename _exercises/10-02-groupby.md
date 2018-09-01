---
layout: exercise
keyword: groupby
episode: 10-aggregations
solution: "
Steps 1. and 2.
\n

```
import pandas as pd
```
\n

```
df_SAFI = pd.read_csv('SAFI_clean.csv', skipinitialspace=True)
```
\n

```
print(df_SAFI.shape)
```
\n

```
print(pd.unique(df_SAFI['rooms']))
```
\n

Step 3.
\n

```
grouped_data = df_SAFI.groupby('rooms')
```
\n

```
grouped_data.describe()
```
\n

Steps 4. and 5.
\n

```
df_SAFI.dropna(inplace=True)
```
\n

```
print(df_SAFI.shape)
```
\n

```
print(pd.unique(df_SAFI['rooms']))
```
\n

```
grouped_data = df_SAFI.groupby('rooms')
```
\n

```
grouped_data.describe()
```
"
---

1. Read in the SAFI_clean.csv dataset.
2. Get a list of the different `rooms` values.
3. Groupby `rooms` and describe the results.
4. Remove all rows with NaN values.
5. repeat steps 2 & 3 and compare the results.