---
layout: exercise
keyword: datedata
episode: 06-date-and-time
solution: "
~~~
from datetime import datetime

format1 = \"%Y-%m-%dT%H:%M:%S.%fZ\"
format2 = \"%d/%m/%Y\"

f = open('SAFI_results.csv', 'r')

line = f.readline()

for line in f:
    A01 = line.split(',')[1]
    A04 = line.split(',')[3]

    datetime_A04 = datetime.strptime(A04, format1)
    datetime_A01 = datetime.strptime(A01, format2)
    date_diff = datetime_A04 - datetime_A01
    print(datetime_A04, datetime_A01, date_diff.days )

f.close()
~~~
{: .language-python}
"
---


1. In the SAFI_results.csv file the A01_interview_date field (index 1) contains a date in the form of 'dd/mm/yyyy'. Read the file and calculate the differences in days (because the interview date is only given to the day) between the A01_interview_date values and the A04_start values. You will need to create a format string for the A01_interview_date field.

2. Looking at the results here and from the previous section of code. Do you think the use of the smartphone data entry system for the survey was being used in real time?
