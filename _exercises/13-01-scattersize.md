---
layout: exercise
keyword: scattersize
episode: 13-matplotlib
solution: "
~~~
# Generate some data for 2 sets of points.
# and additional data for the sizes - suitably scaled
x1 = pd.Series(np.random.rand(20) - 0.5 )
y1 = pd.Series(np.random.rand(20) - 0.5 )
z1 = pd.Series(np.random.rand(20)*200 )

x2 = pd.Series(np.random.rand(20) + 0.5 )
y2 = pd.Series(np.random.rand(20) + 0.5 )
z2 = pd.Series(np.random.rand(20)*200 )

# Add some features
plt.title('Scatter Plot')
plt.ylabel('Range of y values')
plt.xlabel('Range of x values')

# plot the points in a scatter plot
plt.scatter(x1,y1, c='red', label='Red Range', s=z1, alpha=0.5 )  # 's' parameter is the dot size
plt.scatter(x2,y2, c='blue', label='Blue Range', s=z2, alpha=0.5) # 'alpha' is the opacity

plt.legend( loc=4 )
plt.show()
~~~
{: .language-python}
"
---


In the scatterplot the s parameter determines the size of the dots. s can be a simple numeric value, say s=100, which will produce dots all of the same size. However you can pass a list of values (or a pandas Series) to provide sizes for the individual dots. This approach is very common as it allows us to provide an extra variable worth of information on the graph.


1. Modify the code we used for the scatter plot to include a size value for each of the points in the series being plotted. The downside is that some of the smaller dots may be completely covered by the larger dots. To try and highlight when this has happened we can change the opacity of the dots.


2. Find out which parameter controls the opacity of the dots ( clue - it is not called opacity), add it to you code and set it > to a reasonable value .
