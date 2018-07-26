---
layout: exercise
keyword: pdindex
episode: 09-extracting-data
solution: "
~~~
print(df_SN7577[['Q3', 'Q2']])
print(df_SN7577[['Q3', 'Q2', 'Q3']])
print(df_SN7577[['Q33', 'Q2']])
print(df_SN7577[['Q1':'Q3']])
~~~
{: .language-python}

You get an error if you only specify '1'. You need to use ':1' or '0:1' to get the first row returned. The ':' is always required. You can use ':' by itself to return all of the rows
"
---
See what happens when you try each of the following:

1. List the columns you want out of order from the way they appear in the file?
2. What happens if we put the same column name in twice?
3. What does python do if you use a non-existing column name? (a.k.a Typo)
4. Use help to figure out how to select a range of columns
5. How can you select only the first row?
6. What about the last 3 rows?
