---
layout: exercise
keyword: counts
episode: nn
solution: "
```
print(pd.unique(df_SAFI['affect_conflicts']))
```
\n

```
print(df_SAFI['affect_conflicts'].count())
```
\n

We know from when we originally displayed the contents of the `df_SAFI` dataframe that there are 131 rows in it. This matches the value for the `respondent_wall_type` count. The count for `affect_conflicts` however is only 92. If you look at the values in the `affect_conflicts` column using

```
df_SAFI['affect_conflicts']
```

you will see that there are several `NaN` values. `NaN` stands for Not a Number, i.e. the value is missing. There are only 92 non-missing values and this is what is reported by the `count()` method. For numeric variables, this value would also be used in the calculation of the mean and std values.
"
---

1. Get the unique entries for the `affect_conflicts` variable

2. Get the count value for `affect_conflicts` and compare it with the count for `respondent_wall_type`.

3. Why do you think they are different?