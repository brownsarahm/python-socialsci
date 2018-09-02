

```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
df = pd.read_csv("../data/SAFI_results.csv")
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Column1</th>
      <th>A01_interview_date</th>
      <th>A03_quest_no</th>
      <th>A04_start</th>
      <th>A05_end</th>
      <th>A06_province</th>
      <th>A07_district</th>
      <th>A08_ward</th>
      <th>A09_village</th>
      <th>A11_years_farm</th>
      <th>...</th>
      <th>F13_du_look_aftr_cows</th>
      <th>F_liv_count</th>
      <th>G01_no_meals</th>
      <th>_members_count</th>
      <th>_note</th>
      <th>gps:Accuracy</th>
      <th>gps:Altitude</th>
      <th>gps:Latitude</th>
      <th>gps:Longitude</th>
      <th>instanceID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>17/11/2016</td>
      <td>1</td>
      <td>2017-03-23T09:49:57.000Z</td>
      <td>2017-04-02T17:29:08.000Z</td>
      <td>Province1</td>
      <td>District1</td>
      <td>Ward2</td>
      <td>Village2</td>
      <td>11</td>
      <td>...</td>
      <td>no</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>698</td>
      <td>-19.112259</td>
      <td>33.483456</td>
      <td>uuid:ec241f2c-0609-46ed-b5e8-fe575f6cefef</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>17/11/2016</td>
      <td>1</td>
      <td>2017-04-02T09:48:16.000Z</td>
      <td>2017-04-02T17:26:19.000Z</td>
      <td>Province1</td>
      <td>District1</td>
      <td>Ward2</td>
      <td>Village2</td>
      <td>2</td>
      <td>...</td>
      <td>no</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>690</td>
      <td>-19.112477</td>
      <td>33.483416</td>
      <td>uuid:099de9c9-3e5e-427b-8452-26250e840d6e</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>17/11/2016</td>
      <td>3</td>
      <td>2017-04-02T14:35:26.000Z</td>
      <td>2017-04-02T17:26:53.000Z</td>
      <td>Province1</td>
      <td>District1</td>
      <td>Ward2</td>
      <td>Village2</td>
      <td>40</td>
      <td>...</td>
      <td>no</td>
      <td>1</td>
      <td>2</td>
      <td>10</td>
      <td>NaN</td>
      <td>13.0</td>
      <td>674</td>
      <td>-19.112108</td>
      <td>33.483450</td>
      <td>uuid:193d7daf-9582-409b-bf09-027dd36f9007</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>17/11/2016</td>
      <td>4</td>
      <td>2017-04-02T14:55:18.000Z</td>
      <td>2017-04-02T17:27:16.000Z</td>
      <td>Province1</td>
      <td>District1</td>
      <td>Ward2</td>
      <td>Village2</td>
      <td>6</td>
      <td>...</td>
      <td>no</td>
      <td>2</td>
      <td>2</td>
      <td>7</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>679</td>
      <td>-19.112229</td>
      <td>33.483424</td>
      <td>uuid:148d1105-778a-4755-aa71-281eadd4a973</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>17/11/2016</td>
      <td>5</td>
      <td>2017-04-02T15:10:35.000Z</td>
      <td>2017-04-02T17:27:35.000Z</td>
      <td>Province1</td>
      <td>District1</td>
      <td>Ward2</td>
      <td>Village2</td>
      <td>18</td>
      <td>...</td>
      <td>no</td>
      <td>4</td>
      <td>2</td>
      <td>7</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>689</td>
      <td>-19.112217</td>
      <td>33.483425</td>
      <td>uuid:2c867811-9696-4966-9866-f35c3e97d02d</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 55 columns</p>
</div>




```python
df.C06_rooms.mean()
```




    1.7404580152671756




```python
df.C06_rooms.hist(bins=4)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f24ce74e390>




![png](output_4_1.png)



```python
df.C06_rooms.hist(bins=40)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f24cc684470>




![png](output_5_1.png)



```python
df.columns
```




    Index(['Column1', 'A01_interview_date', 'A03_quest_no', 'A04_start', 'A05_end',
           'A06_province', 'A07_district', 'A08_ward', 'A09_village',
           'A11_years_farm', 'A12_agr_assoc', 'B11_remittance_money',
           'B16_years_liv', 'B17_parents_liv', 'B18_sp_parents_liv',
           'B19_grand_liv', 'B20_sp_grand_liv', 'B_no_membrs',
           'C01_respondent_roof_type', 'C02_respondent_wall_type',
           'C02_respondent_wall_type_other', 'C03_respondent_floor_type',
           'C04_window_type', 'C05_buildings_in_compound', 'C06_rooms',
           'C07_other_buildings', 'D_plots_count', 'E01_water_use',
           'E17_no_enough_water', 'E19_period_use', 'E20_exper_other',
           'E21_other_meth', 'E23_memb_assoc', 'E24_resp_assoc', 'E25_fees_water',
           'E26_affect_conflicts', 'E_no_group_count', 'E_yes_group_count',
           'F04_need_money', 'F05_money_source_other', 'F06_crops_contr',
           'F08_emply_lab', 'F09_du_labour', 'F10_liv_owned_other', 'F12_poultry',
           'F13_du_look_aftr_cows', 'F_liv_count', 'G01_no_meals',
           '_members_count', '_note', 'gps:Accuracy', 'gps:Altitude',
           'gps:Latitude', 'gps:Longitude', 'instanceID'],
          dtype='object')




```python
df.groupby('C02_respondent_wall_type').C01_respondent_roof_type.count()
```




    C02_respondent_wall_type
    burntbricks    67
    cement          1
    muddaub        46
    sunbricks      17
    Name: C01_respondent_roof_type, dtype: int64




```python
df.groupby('C02_respondent_wall_type').C01_respondent_roof_type.hist()
```




    C02_respondent_wall_type
    burntbricks    AxesSubplot(0.125,0.125;0.775x0.755)
    cement         AxesSubplot(0.125,0.125;0.775x0.755)
    muddaub        AxesSubplot(0.125,0.125;0.775x0.755)
    sunbricks      AxesSubplot(0.125,0.125;0.775x0.755)
    Name: C01_respondent_roof_type, dtype: object




![png](output_8_1.png)



```python
df[ ["gps:Latitude", "gps:Longitude"] ].plot.scatter()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-69f4c2733b18> in <module>()
    ----> 1 df[ ["gps:Latitude", "gps:Longitude"] ].plot.scatter()
    

    TypeError: scatter() missing 2 required positional arguments: 'x' and 'y'



```python
df.plot.scatter(x='gps:Latitude', y='gps:Longitude', c='gps:Altitude', colormap="viridis", figsize=[4,4])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f24cc479b38>




![png](output_10_1.png)



```python
# %load code/plots
# Make a scatter plot of 'A11_years_farm' vs 'B16_years_liv' and color the points
# by 'C05_buildings_in_compound'
#


# Make a bar plot of the mean number of rooms per wall type

# extension: try by wall and roof type?

```


```python
df.groupby("C02_respondent_wall_type")["C06_rooms"].mean()
```




    C02_respondent_wall_type
    burntbricks    2.104478
    cement         3.000000
    muddaub        1.260870
    sunbricks      1.529412
    Name: C06_rooms, dtype: float64




```python
ax = df.groupby("C02_respondent_wall_type")["C06_rooms"].mean().plot(kind="barh")
```


![png](output_13_0.png)



```python
import seaborn as sns
sns.set(font_scale=1.5)

ax = df.groupby("C02_respondent_wall_type")["C06_rooms"].mean().plot(kind="barh", 
                                                                     title="Title of the plot",
                                                                     xlim=[0,10])

plt.savefig("rooms.png")
plt.savefig("rooms.pdf", bbox_inches="tight", dpi=600)
plt.show()
```


![png](output_14_0.png)



```python
sns.barplot(data=df, x="C01_respondent_roof_type", y="C06_rooms")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2846e096240>




![png](output_15_1.png)



```python
df.groupby(["C01_respondent_roof_type", "C02_respondent_wall_type"])["C06_rooms"].mean()
```




    C01_respondent_roof_type  C02_respondent_wall_type
    grass                     burntbricks                 1.681818
                              muddaub                     1.214286
                              sunbricks                   1.111111
    mabatipitched             burntbricks                 2.166667
                              muddaub                     2.000000
                              sunbricks                   2.000000
    mabatisloping             burntbricks                 2.333333
                              cement                      3.000000
                              muddaub                     1.000000
                              sunbricks                   2.000000
    Name: C06_rooms, dtype: float64




```python
df.groupby(["C01_respondent_roof_type", "C02_respondent_wall_type"])["C06_rooms"].mean().plot(kind="barh")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2846c1290b8>




![png](output_17_1.png)



```python
df.columns
```




    Index(['Column1', 'A01_interview_date', 'A03_quest_no', 'A04_start', 'A05_end',
           'A06_province', 'A07_district', 'A08_ward', 'A09_village',
           'A11_years_farm', 'A12_agr_assoc', 'B11_remittance_money',
           'B16_years_liv', 'B17_parents_liv', 'B18_sp_parents_liv',
           'B19_grand_liv', 'B20_sp_grand_liv', 'B_no_membrs',
           'C01_respondent_roof_type', 'C02_respondent_wall_type',
           'C02_respondent_wall_type_other', 'C03_respondent_floor_type',
           'C04_window_type', 'C05_buildings_in_compound', 'C06_rooms',
           'C07_other_buildings', 'D_plots_count', 'E01_water_use',
           'E17_no_enough_water', 'E19_period_use', 'E20_exper_other',
           'E21_other_meth', 'E23_memb_assoc', 'E24_resp_assoc', 'E25_fees_water',
           'E26_affect_conflicts', 'E_no_group_count', 'E_yes_group_count',
           'F04_need_money', 'F05_money_source_other', 'F06_crops_contr',
           'F08_emply_lab', 'F09_du_labour', 'F10_liv_owned_other', 'F12_poultry',
           'F13_du_look_aftr_cows', 'F_liv_count', 'G01_no_meals',
           '_members_count', '_note', 'gps:Accuracy', 'gps:Altitude',
           'gps:Latitude', 'gps:Longitude', 'instanceID'],
          dtype='object')


