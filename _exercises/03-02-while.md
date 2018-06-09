---
layout: exercise
keyword: while
episode: 03-control-structures
solution: "
1. Because i is incremented before the sum, you are summing 1 to 11.
2. The Boolean value is set to False the loop will never be executed.
3. When i does equal 10 the expression is False and the loop does not execute so we have only summed 1 to 9
4. Because you cannot guarantee the internal representation of Float, you should never try to compare them for equality. In this particular case the i never 'equals' n and so the loop never ends. - If you did try running this, you can stop it using <kbd>Ctrl</kbd>+<kbd>c</kbd> in a terminal or going to the kernel menu of a notebook and choosing interrupt.
"
---

In the examples below, without running them try to predict why we will not get the desired answer.
Run each, one at a time, and then correct them. Remember that when the input next to a notebook cell is `[*]`` your python interpreter is still working.

~~~
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
# sum of n  numbers
i = 0
while  i <= n :
   i = i + 1
   cur_sum = cur_sum + i

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
~~~
{: .language-python}

~~~
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
boolvalue = False
# sum of n  numbers
i = 0
while  i <= n and boolvalue:
   cur_sum = cur_sum + i
   i = i + 1

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
~~~
{: .language-python}

~~~
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
# sum of n  numbers
i = 0
while  i != n :
   cur_sum = cur_sum + i
   i = i + 1

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
~~~
{: .language-python}

~~~
# while loop - summing the numbers 1.1 to 9.9 i. steps of 1.1
n = 9.9
cur_sum = 0
# sum of n  numbers
i = 0
while  i != n :
   cur_sum = cur_sum + i
   i = i + 1.1
   print(i)

print("The sum of the numbers from 1.1 to", n, "is ", sum)
~~~
{: .language-python}
