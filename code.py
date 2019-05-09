# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

data = data.rename(columns = {'Total' : 'Total_Medals'})

print(data.head(10))

#Code starts here



# --------------
#Code starts here

#data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', (data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both'))

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both'))

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(index = 146, inplace = True)

#print(top_countries.tail())

def top_ten (df, col) :
    country_list = []
    top_10 = df.nlargest(10, col)
    country_list = list(top_10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(set(top_10_summer).intersection(top_10_winter)).intersection(top_10))

print(common)






# --------------
#Code starts here

#For Summer

#Creating the dataframe for Summer event
summer_df= data[data['Country_Name'].isin(top_10_summer)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

#Changing the graph title
plt.title('Top 10 Summer')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')


#For Winter

#Creating the dataframe for Winter event
winter_df=data[data['Country_Name'].isin(top_10_winter)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

#Changing the graph title
plt.title('Top 10 Winter')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')



#For both the events

#Creating the dataframe for both the events
top_df=data[data['Country_Name'].isin(top_10)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

#Changing the graph title
plt.title('Top 10')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')





# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_df.set_index('Country_Name', inplace = True)
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df['Golden_Ratio'].idxmax()

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_df.set_index('Country_Name', inplace = True)
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Golden_Ratio'].idxmax()

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_df.set_index('Country_Name', inplace = True)
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Golden_Ratio'].idxmax()

print(summer_max_ratio, summer_country_gold, winter_max_ratio, winter_country_gold, top_max_ratio, top_country_gold)


# --------------
#Code starts here

data_1 = data[: -1]
data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total'] * 1

#data_1.set_index('Country_Name', inplace = True)

#most_points = data_1['Total_Points'].max()

#best_country = data_1['Total_Points'].idxmax()

most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(most_points, best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

print(best)

best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]

best.plot.bar()

plt.xlabel('United States')
plt.ylabel('Tally')
plt.xticks(rotation = 45)


