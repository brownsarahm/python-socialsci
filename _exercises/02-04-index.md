---
layout: exercise
keyword: index
episode: 02-basics
solution: |
  ~~~
  list7_2 = list(range(2, 11, -2))  
  print(list7)
  ~~~
  {: .language-python}
  a negative step size increments backwards, but the start has to be higher than
   the stop for it to work.  As written, it outputs nothing because starting at
  2, and stepping backwards 2 is already less than 11.

  ~~~
  list(range(10, 1, -2))  
  ~~~
  {: .language-python}
hint: |
  try other values for the start and stop to explore what the negative step does
---

~~~
list7_2 = list(range(2, 11, -2))
~~~
{: .language-python}

1. Predict what the value of `list7_2` will be, is it what you expected? Summarize what a negative step value does.

2. Create a list using the range() function which contains the even numbers between 1 and 10 in reverse order ([10,8,6,4,2])
