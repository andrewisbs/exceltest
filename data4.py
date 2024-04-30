import pandas as pd

# Load the dataset to see the first few rows and understand its structure
data_path = 'RAP_Journal_Engagement.csv'
df = pd.read_csv(data_path)

# Display the first few rows of the dataframe
df.head()

# Calculate the number of returning users
df['Returning users'] = df['Users'] - df['New users']

# Summarize the data to get total counts and averages for new and returning users across all regions
summary_metrics = df.groupby(['Region']).agg(
    Total_Users=pd.NamedAgg(column='Users', aggfunc='sum'),
    New_Users=pd.NamedAgg(column='New users', aggfunc='sum'),
    Returning_Users=pd.NamedAgg(column='Returning users', aggfunc='sum'),
    Total_Engaged_Sessions=pd.NamedAgg(column='Engaged sessions', aggfunc='sum'),
    Average_Engagement_Rate=pd.NamedAgg(column='Engagement rate', aggfunc='mean'),
    Average_Engaged_Sessions_Per_User=pd.NamedAgg(column='Engaged sessions per user', aggfunc='mean'),
    Average_Engagement_Time_Seconds=pd.NamedAgg(column='Average engagement time (seconds)', aggfunc='mean'),
    Total_Event_Count=pd.NamedAgg(column='Event count', aggfunc='sum')
).reset_index()

summary_metrics.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Setting up the figure and axes for the plots
fig, ax = plt.subplots(3, 1, figsize=(10, 18))

# Engagement Rate by Region
sns.barplot(x='Average_Engagement_Rate', y='Region', data=summary_metrics.sort_values(by='Average_Engagement_Rate', ascending=False), ax=ax[0])
ax[0].set_title('Average Engagement Rate by Region')
ax[0].set_xlabel('Average Engagement Rate')
ax[0].set_ylabel('Region')

# Average Engagement Time by Region
sns.barplot(x='Average_Engagement_Time_Seconds', y='Region', data=summary_metrics.sort_values(by='Average_Engagement_Time_Seconds', ascending=False), ax=ax[1])
ax[1].set_title('Average Engagement Time (Seconds) by Region')
ax[1].set_xlabel('Average Engagement Time (Seconds)')
ax[1].set_ylabel('Region')

# Event Count by Region
sns.barplot(x='Total_Event_Count', y='Region', data=summary_metrics.sort_values(by='Total_Event_Count', ascending=False), ax=ax[2])
ax[2].set_title('Total Event Count by Region')
ax[2].set_xlabel('Total Event Count')
ax[2].set_ylabel('Region')

plt.tight_layout()
plt.show()
                  