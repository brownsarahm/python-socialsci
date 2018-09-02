---
title: "Data visualisation using Matplotlib"
teaching: 25
exercises: 25
questions:
- "How can I create visualisations of my data?"
objectives:
- "Import pyplot from the matplotlib library"
- "Create simple plots using pyplot"
keypoints:
- "Graphs can be drawn directly from pandas, but it still uses matplotlib"
- "Different graph types have different data requirements"
- "Graphs are created from a variety of discrete components placed on a 'canvas', you don't have to use them all"
- "Plotting multiple graphs on a single 'canvas' is possible"
---

## Plotting in python

There are a wide variety of ways to plot in python, like many programming languages.  Some do more of the design work for you and others let you customize the look of the plots and all of the little details yourself. `Pandas` has basic plots built into it that reduce the amount of syntax, if your data is already in a DataFrame.  `matplotlib` is fully controllable down to basic elements and includes a module `pylab` that is somewhere in between (designed to feel like matlab plotting, if you happen to have done that before)

## Plotting with Pandas

To plot with pandas we have to import it as we have done in past episodes.  We can also use the `%matplotlib inline` notebook magic to reduce syntax otherwise.  Without that we need to a `show()` command

~~~
import pandas as pd
%matplotlib inline
~~~
{: .language-python}

We also need data to work with loaded into a DataFrame and it's helpful to look at a few rows to remember what's there.

~~~
df = pd.read_csv("../data/SAFI_results.csv")
df.head()
~~~
{: .language-python}

Next, we can plot the a histogram of a variable


~~~
{: .language-python}
df.C06_rooms.hist(bins=4)
~~~~~~
{: .language-python}

![png](output_4_1.png)


We can change the number of bins to make it look how we would like, for example

~~~
{: .language-python}
df.C06_rooms.hist(bins=40)
~~~~~~
{: .language-python}

![png](output_5_1.png)

Pandas plottingn also works on groupbys

~~~
{: .language-python}
df.groupby('C02_respondent_wall_type').C01_respondent_roof_type.hist()
~~~~~~
{: .language-python}
![png](output_8_1.png)


There is also scatter plots


~~~
{: .language-python}
df.plot.scatter(x='gps:Latitude', y='gps:Longitude', c='gps:Altitude', colormap="viridis", figsize=[4,4])
~~~~~~
{: .language-python}

![png](output_10_1.png)





## Matplotlib

Matplotlib is a Python graphical library that can be used to produce a variety of different graph types.

The pandas library contains very tight integration with matplotlib. There are functions in pandas that automatically call matplotlib functions to produce graphs.

Although we are using Matplotlib in this episode, pandas can make use of several other graphical libraries available from within Python such as ggplot2 and seaborn.

## Importing matplotlib

The matplotlib library can be imported using any of the import techniques we have seen. As `pandas` is generally imported with `import pandas as pd`, you will find that `matplotlib` is most commonly imported with `import matplotlib.pylab as plt` where 'plt' is the alias.

In addition to importing the library, in a Jupyter notebook environment we need to tell Jupyter that when we produce a graph we want it to be display the graph in a cell in the notebook just like any other results. To do this we use the `%matplotlib inline` directive.  

If you forget to do this, you will have to add `plt.show()` to see the graphs.

~~~
import matplotlib.pyplot as plt
%matplotlib inline
~~~
{: .language-python}

Internally the pandas 'plot' method has called the 'bar' method of matplotlib and provided a set of parameters, including the pandas.Series s to generate the graph.

We can use matplotlib directly to produce a similar graph. In this case we need to pass two parameters, the number of bars we need and the pandas Series holding the values.

We also have to explicitly call the `show()` function to produce the graph.

## Histograms

We can plot histograms in a similar way, directly from pandas and also from Matplotlib

The pandas way

~~~
# plot the bar chart
df.C06_rooms.hist(bins=40)
~~~
{: .language-python}

and the matplotlib way

~~~
plt.hist(s)
plt.show()
~~~
{: .language-python}

For the Histogram, each data point is allocated to 1 of 10 (by default) equal 'bins' of equal size (range of numbers) which are indicated along the x axis and the number of points (frequency) is shown on the y axis.

In this case the graphs are almost identical. The only difference being in the first graph the y axis has a label 'Frequency' associated with it.

We can fix this with a call to the `ylabel` function

~~~
plt.ylabel('Frequency')
plt.hist(s)
plt.show()
~~~
{: .language-python}

In general most graphs can be broken down into a series of elements which, although typically related in some way, can all exist independently of each other. This allows us to create the graph in a rather piecemeal fashion.

The labels (if any) on the x and y axis are independent of the data values being represented. The title and the legend are also independent objects within the overall graph.

In matplotlib you create the graph by providing values for all of the individual components you choose to include. When you are ready, you call the `show` function.

Using this same approach we can plot two sets of data on the same graph

We will use a scatter plot to demonstrate some of the available features.

For a scatter plot we need two sets of data points one for the x values
and the other for the y values.

## Scatter plot

The scatter plot requires the x and y coordinates of each of the points being plotted.
To provide this we will generate two series of random data one for the x coordinates and the other for the y coordinates

We will generate two sets of points and plot them on the same graph.

We will also add other common features like a title, a legend and labels on the x and y axis.

~~~
# Generate some date for 2 sets of points.
x1 = pd.Series(np.random.rand(20) - 0.5 )
y1 = pd.Series(np.random.rand(20) - 0.5 )

x2 = pd.Series(np.random.rand(20) + 0.5 )
y2 = pd.Series(np.random.rand(20) + 0.5 )


# Add some features
plt.title('Scatter Plot')
plt.ylabel('Range of y values')
plt.xlabel('Range of x values')

# plot the points in a scatter plot
plt.scatter(x1,y1, c='red', label='Red Range' )  # 'c' parameter is the colour and 'label' is the text for the legend
plt.scatter(x2,y2, c='blue', label='Blue Range')

plt.legend( loc=4 )  # the locations 1,2,3 and 4 are top-right, top-left, bottom-left and bottom-right
# Show the graph with the two sets of points
plt.show()
~~~
{: .language-python}

In the call to the `scatter` method, the `label` parameter values are used by the _legend_.
The `c` or `color` parameter can be set to any color matplotlib recognises. Full details of the available colours are available in the [matplotlib](http://matplotlib.org/api/colors_api.html) website. The [markers](http://matplotlib.org/api/markers_api.html) section will tell you what markers you can use instead of the default 'dots'. There is also an `s` (size) parameter which allows you to change the size of the marker.


{% include exercise_output.html keyword="scattersize" %}


## Boxplot

A boxplot provides a simple representation of a variety of statistical qualities of a single set of data values.

![box_plot](../fig/vis_boxplot_01.png)

~~~
x = pd.Series(np.random.standard_normal(256))

# Show a boxplot of the data
plt.boxplot(x)
plt.show()
~~~
{: .language-python}

A common use of the boxplot is to compare the statistical variations across a set of variables.

The variables can be an independent series or columns of a Dataframe.

~~~
df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE')) # creating a Dataframe directly with pandas
plt.boxplot(df.A, labels = 'A')
plt.show()
~~~
{: .language-python}

> ## Exercise
>
> Can you change the code above so that columns `A` , `C` and `D` are all displayed on the same graph?
>
> > ## Solution
> >
> > ~~~
> > df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE'))
> > plt.boxplot([df.A, df.C, df.D], labels = ['A', 'C', 'D'])
> > plt.show()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

The boxplot function cannot accept a whole Dataframe. The code

~~~
df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE'))
plt.boxplot(df)
plt.show()
~~~
{: .language-python}

will fail.

However we can use the pandas plot method

~~~
df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE'))
df.plot(kind = 'box', return_type='axes') # the return_type='axes' is only needed for forward compatibility
~~~
{: .language-python}

We can add a title to the above by adding the `title` parameter. However there are no parameters for adding the axis labels.
To add labels we can use matplotlib directly.

~~~
df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE'))
df.plot(kind = 'box', return_type='axes')

plt.title('Box Plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()
~~~
{: .language-python}

## Saving a graph

If you wish to save your graph as an image you can do so using the `savefig()` function. The image can be saved as a pdf, jpg or png file by changing the file extension.

~~~
df = pd.DataFrame(np.random.normal(size=(100,5)), columns=list('ABCDE'))
df.plot(kind = 'box', return_type='axes')

plt.title('Box Plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
#plt.show()
plt.savefig('boxplot_from_df.pdf')
~~~
{: .language-python}
