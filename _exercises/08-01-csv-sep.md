---
layout: exercise
keyword: csv-sep
episode: 08-Pandas
solution: "
```
SAFI_oops = pd.read_csv('SAFI_clean.csv', sep = '\\t')
```
\n

```
print(SAFI_oops.shape)
```
\n

```
print(SAFI_oops)
```
\n

If you use a separation character that is not used in the data, then each record will be treated as a single column. So the shape is given as 131 rows (correct) but only one column.
When the contents is displayed the only column name is the complete first record.
"
---
What happens if you specify the tab character as column separator with `sep='\t'`?