import pandas as pd
import numpy as np

# Import the CVS from custom 'All My Tickets View'
df = pd.read_csv('test.csv',
    parse_dates=['Requested','Updated'])

# To Drop COlumns:
# newdf = df.drop(columns = ['Column Name])

# Use to_string() to print the entire DataFrame
# without .to_string(), Pandas will only return the first + last 5 rows
print('Info')
print(df.info())

# Next Step is to create a function
# Switch case?
# if ('Status'='Open') {'Next Comment Date'=df[]}


df['Next Due Date'] = df['Requested'] + np.timedelta64(2,'D')

df.loc[df['Status'].str.strip()=='New', 'Next Due Date'] = df['Requested']
df.loc[df['Status'].str.strip()=='Open', 'Next Due Date'] = df['Updated'] + np.timedelta64(2,'D')
df.loc[df['Status'].str.strip()=='Pending', 'Next Due Date'] = df['Updated'] + np.timedelta64(2,'D')
df.loc[df['Status'].str.strip()=='Solved', 'Next Due Date'] = 0


# Create the URL based off ID
df['Help Center Link'] = 'https://liferay-support.zendesk.com/agent/tickets/' + df['ID'].astype(str)



print('---')
print('Help Center Added')
print(df.to_string())

df.to_csv('./formatted/test_formatted.csv', index=False, encoding='utf-8')