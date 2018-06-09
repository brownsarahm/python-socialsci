---
layout: exercise
keyword: dfinfo
episode: 08-Pandas
solution: "
~~~
for name in df_SN7577.columns:
    print(name)
~~~
{: .language-python}

Challenge

~~~
for name, dtype in zip(df_SN7577.columns,df_SN7577.dtypes):
    print (name, dtype)
~~~
"
---

When we asked for the column names and their datatypes, the output was abridged, i.e. we didn't get the values for all of the columns. Can you write a small piece of code which will return all of the values

Challenge: Modify your program to output both the name and the dataype for each column. (hint: use help on the builtin `zip()` function)
