---
layout: exercise
name: notebook
episode: 02-basics
solution: "1. Only the last result is printed.

2. The 4 'items' are printed by the REPL, but not in the same way as the print statement. The items in quotes are treated as separate strings, for the variables a and b the values are printed. All four items are treated as a 'tuple' which are shown in parentheses, a tuple is another datatype in Python that allows you to group things together and treat as a unit. We can tell that it is a tuple because of the `()`


A complete set of Python operators can be found in the [official documentation](https://docs.python.org/3.5/library/operator.html) . The documentataion may \"appear\" a bit confusing as it initially talks about operators as functions whereas we generally use them as 'inplace ' operators. Section 10.3.1 provides a table which list all of the available operators, not all of which are relevant to basic arithmetic."
---

Example code:
~~~
print("a =", a, "and b =" , b)
print(a + b)      # addition
print(a * b)      # multiplication
print(a - b)      # subtraction
print(a / b)      # division
print(b ** a)     # exponentiation
print(2 * a % b)  # modulus - returns the remainder
~~~

1. Create a new cell and paste into it the assignments to the variables a and b and the contents of the code above. Remove all of the calls to the print function so you only have the expressions that were to be printed and run the code. What is returned?

2. Make a new cell with only `("a =", a, "and b =" , b)` in it. How does this output differ from when we used the print function?

3. Practice assigning values to variables using as many different operators as you can think of.

4. Create some expressions to be evaluated using parentheses to enforce the order of mathematical operations that you require
