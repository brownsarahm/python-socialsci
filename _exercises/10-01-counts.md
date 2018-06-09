---
layout: exercise
keyword: counts
episode: nn
solution: "
1. We know from when we originally displayed the contents of the `df_SAFI` dataframe that there are 131 rows in it. This matches the value for the `B_no_membrs` count. The count for `E19_period_use` however is only 92. If you look at the values in the `E19_period_use` column using

~~~
df_SAFI['E19_period_use']
~~~
{: .language-python}

you will see that there are several `NaN` values. They also occurred when we used `describe()` on the full dataframe. `NaN` stands for Not a Number, ie. the value is missing. There are only 92 non-missing values and this is what is reported by the `count()` method. This value is also used in the calculation of the mean and std values.
"
---


Compare the count values returned for the `B_no_membrs` and the `E19_period_use` variables.

1. How can you investigate why they're different?
2. How does this affect the calculation of the mean values?
