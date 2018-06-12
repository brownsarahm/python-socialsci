---
layout: exercise
keyword: datemath
episode: 06-date-and-time
solution: "
~~~
date_diff = datetime_start - datetime_end
print(type(date_diff))
print(date_diff)
~~~
{: .language-python}


~~~
<class 'datetime.timedelta'>
-11 days, 16:20:49
~~~
{: .output}
"
---

What happens if you subtract in the opposite order( that is start-end)? Why?
