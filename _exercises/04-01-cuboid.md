---
layout: exercise
keyword: cuboid
episode: 04-resuable
solution: "
~~~
def cuboid(H,W,L):
    vol = H*W*L
    sa = 2*(H*W + H*L + L*W)
    edges = 4*(H + W + L)
    return vol, sa, edges
volume, surface_area, length_of_edges = cuboid(2,3,4)
print('Volume = ', volume, ' Surface_area = ', surface_area, ' Sum of edges = ', length_of_edges)
~~~
{: .language-python}

The cuboid function above returns all three values from a single call. This means that you need three variables in which to place the 3 returned values. If you do not provide three variables, you will get an error.
Unless you are always going to use the 3 values, it would probably be better in this case to use distinct functions for these three cases.

"
---

1. Write a function definition to calculate the volume of a cuboid. The function will use three parameters 'H', 'W' and 'L' and return the volume.

2. Supposing that in addition to the volume I also wanted to calculate the surface area and the sum of all of the edges. Would I (or should I) have three separate functions or could I write a single function to provide all three values together?
