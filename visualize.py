###################################################################################################
#   Program to visualize the crime data into a trend chart, bar graph and pie chart respectively. #
#   Written by Sahil Hussain                                                                      #
###################################################################################################

import pandas as pd
import matplotlib.pyplot as plotter

# trend chart
data = pd.read_csv('crime-data.csv')
data.set_index('CRIME HEAD', inplace=True)
data = data.transpose()

plotter.figure(figsize=(12, 6))
plotter.title('Crime Trends Between 2001-2010')
plotter.xlabel('Year')
plotter.ylabel('Number of Incidents')
for column in data.columns:
    plotter.plot(data.index, data[column], label=column)
plotter.xticks(rotation=45)
plotter.legend(loc='upper left', bbox_to_anchor=(1, 1))

# bar graph
data = pd.read_csv('crime-data.csv')
years = data.columns[1:]
crime_data = data.loc[data['CRIME HEAD'] == 'TOTAL IPC', years]

plotter.figure(figsize=(12, 6))
plotter.bar(years, crime_data.values[0], color='blue')
plotter.xlabel('Year')
plotter.ylabel('Total IPC Cases')
plotter.title('Total IPC Cases Over the Years (2001-2010)')
plotter.xticks(rotation=45)
plotter.tight_layout()

plotter.show()

# pie chart
data = pd.read_csv('crime-data.csv')

crime_head = data['CRIME HEAD']
data = data.iloc[:, 1:]


def label_function(val):
    if val < 1:
        return ''
    return f'{val:.1f}%'


fig, ax = plotter.subplots(figsize=(10, 10))
wedges, labels, autopct_text = ax.pie(data.sum(
    axis=1), labels=crime_head, autopct=label_function, startangle=90, labeldistance=None)
ax.axis('equal')
ax.legend(loc='best', labels=crime_head[data.sum(axis=1) > 2])
plotter.title('Crime in New Delhi between 2001 and 2010')

for text in autopct_text:
    text.set_text('')

plotter.show()
