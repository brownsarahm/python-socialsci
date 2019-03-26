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

There are a variety of ways to plot in python, like many programming languages.  Some of these options do more of the design work for you and others leave controlling the aesthetic of the plots and all of the little details yourself. First, we'll look at the one that's the least new syntax, then we'll use of of the more flexible ones to customize our plots in common ways for publication ready graphics. `Pandas` has basic plots built into it that reduce the amount of syntax, if your data is already in a DataFrame.
Matplotlib is a Python graphical library that can be used to produce a variety of different graph types and is fully controllable down to basic elements.  


The pandas library contains very tight integration with matplotlib. There are functions in pandas that automatically call matplotlib functions to produce graphs.

Although we are using Matplotlib in this episode, pandas can make use of several other graphical libraries available from within Python such as ggplot2 and seaborn. Seaborn has some very powerful features and advancecd plot types.  One of its most useful features is formatting.

## Plotting with Pandas

To plot with pandas we have to import it as we have done in past episodes.  We can also use the `%matplotlib inline` notebook magic to reduce syntax otherwise.  Without that we need to a `show()` command

~~~
import pandas as pd
%matplotlib inline
~~~
{: .language-python}

We also need data to work with loaded into a DataFrame and it's helpful to look at a few rows to remember what's there.

~~~
df = pd.read_csv("data/SAFI_full_shortname.csv")
df.head()
~~~
{: .language-python}

Next, we can plot the a histogram of a variable


~~~
safi_df['years_liv'].hist()
~~~
{: .language-python}

![png](output_4_1.png)


We can change the number of bins to make it look how we would like, for example

~~~
safi_df['years_liv'].hist(bins=20)
~~~
{: .language-python}


We can also specify the column as a parameter and a groupby column with the `by` keyword. there are a lot of keywords available to make it look better, we can see some of the most likely ones (as decided by pandas developers) by using <kbd>shift</kbd> + <kbd>tab<kbd>. Lets try `layout`, `figsize`, and `sharex`.

~~~
safi_df.hist(column='years_liv',by='village',layout=(1,3),figsize=(12,3),sharex=True)
~~~
{: .language-python}

## Scatter plot

The scatter plot requires the x and y coordinates of each of the points being plotted.
To provide this we will generate two series of random data one for the x coordinates and the other for the y coordinates

We will generate two sets of points and plot them on the same graph.

We will also add other common features like a title, a legend and labels on the x and y axis.

~~~
{: .language-python}
df.plot.scatter(x='gps:Latitude', y='gps:Longitude', c='gps:Altitude', colormap="viridis", figsize=[4,4])
~~~~~~
{: .language-python}

![png](output_10_1.png)



{% include exercise_output.html keyword="pdplot" %}



## Boxplot

A boxplot provides a simple representation of a variety of statistical qualities of a single set of data values.

![box_plot](../fig/vis_boxplot_01.png)

A common use of the boxplot is to compare the statistical variations across a set of variables.

The variables can be an independent series or columns of a Dataframe using the pandas plot method

~~~
safi_df.boxplot(by ='village',column=['buildings_in_compound'])
~~~
{:.language-python}

We can make it look prettier with seaborn, much more easily than fixing components manually with matplotlib.
~~~
import seaborn as sns
sns.boxplot(data=safi_df,x ='village',y='buildings_in_compound')
~~~
{: .language-python}


~~~
sns.lmplot(x='years_farm', y='years_liv',data=safi_df,hue='village')
~~~
{: .language-python}

## Matplotlib

If we want to do more advanced or lower level things with our plots, we need to use matplotlib directly, not through pandas.  First we need to import it.


The matplotlib library can be imported using any of the import techniques we have seen. `Matplotlib` includes a module `pylab` that offers an interface between that of base matplolib and pandas in terms of the level of the components that you have to specify that is most often the level at which the packages is used (it's also designed to feel like MATLAB plotting, if you happen to have done that before).
As `pandas` is generally imported with `import pandas as pd`, you will find that `matplotlib` is most commonly imported with `import matplotlib.pylab as plt` where 'plt' is the alias.

~~~
import matplotlib.pyplot as plt
~~~
{: .language-python}

In addition to importing the library, in a Jupyter notebook environment we need to tell Jupyter that when we produce a graph we want it to be display the graph in a cell in the notebook just like any other results. To do this we use the `%matplotlib inline` ipython magic function.  

Without this optional magic, or in a base python interpreter matplotlib requires calling the `plt.show()` function to see the graphs.

~~~
%matplotlib inline
~~~
{: .language-python}

Above, internally the pandas 'plot' method has called the 'bar' method of matplotlib and provided a set of parameters, including the pandas.Series s to generate the graph. 

We can use matplotlib directly to produce a similar graph. In this case we need to pass two parameters, the number of bars we need and the pandas Series holding the values.

We also have to explicitly call the `show()` function to produce the graph.

In general most graphs can be broken down into a series of elements which, although typically related in some way, can all exist independently of each other. This allows us to create the graph component by component.

The labels (if any) on the x and y axis are independent of the data values being represented. The title and the legend are also independent objects within the overall graph.

In Matplotlib you create the graph by providing values for all of the individual components you choose to include. When you are ready, you call the `show` function.

Using this same approach we can plot two sets of data on the same graph

We will use a scatter plot to demonstrate some of the available features.


## Saving Plots

~~~
plt.savefig("rooms.png")
plt.savefig("rooms.pdf", bbox_inches="tight", dpi=600)
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


{% include exercise_output.html keyword="niceplot" %}
