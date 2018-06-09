---
layout: exercise
keyword: groupby
episode: 10-aggregations
solution: "
~~~
# Steps 1 and 2
import numpy as np
df_SAFI = pd.read_csv(\"SAFI_results.csv\")
print(df_SAFI.shape)
print(pd.unique(df_SAFI['C01_respondent_roof_type']))
~~~
{: .language-python}

~~~
# Step 3
grouped_data = df_SAFI.groupby('C01_respondent_roof_type')
grouped_data.describe()
~~~
{: .language-python}

~~~
# steps 4 and 5
df_SAFI = df_SAFI[(df_SAFI['E_no_group_count'].notnull())]
grouped_data = df_SAFI.groupby('C01_respondent_roof_type')
print(df_SAFI.shape)
print(pd.unique(df_SAFI['C01_respondent_roof_type']))
grouped_data.describe()
~~~
{: .language-python}

'E_no_group_count' is related to whether or not farm plots are irrigated or not. It has no obvious connection to farm buildings.
By restricting the data to non-irrigated plots we have accidentally? removed one of the roof_types completely.
"
---

1. Read in the SAFI_results.csv dataset.
2. Get a list of the different 'C01_respondent_roof_type' values.
3. Groupby 'C01_respondent_roof_type' and describe the results.
4. Remove rows with NULL values for 'E_no_group_count'.
5. repeat steps 2 & 3 and compare the results.
