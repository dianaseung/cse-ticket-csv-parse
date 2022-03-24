import pandas as pd
import numpy as np

# Import the CVS from custom 'All My Tickets View'
df = pd.read_csv('test.csv',
    parse_dates=['Requested','Updated'])

# To Drop Columns without changing the original CSV:
# newdf = df.drop(columns = ['Next SLA breach'])

# Use to_string() to print the entire DataFrame
# without .to_string(), Pandas will only return the first + last 5 rows
print('Initial DataFrame')
print(df.to_string())


# To see datatypes of columns
# print('DataType Info')
# print(df.info())


# Next Step is to check status
# and conditionally return new values based on Requested or Updated values

# By default, Next Due Date will be set to 2 days from Requested date
# These values hold true for Updater=='Responder'
df['Next Due Date'] = df['Requested'] + np.timedelta64(2,'D')

df.loc[df['Status'].str.strip()=='New', 'Next Due Date'] = df['Requested']
df.loc[df['Status'].str.strip()=='Open', 'Next Due Date'] = df['Updated'] + np.timedelta64(2,'D')
df.loc[df['Status'].str.strip()=='Pending', 'Next Due Date'] = df['Updated'] + np.timedelta64(2,'D')
df.loc[df['Status'].str.strip()=='Solved', 'Next Due Date'] = 0

# Next step would be if Update=='Agent'
# But I'm not sure if it really changes anything because we would still want to follow-up within X days
# Double check timelines before working on this portion

# Auto-generate 'Help Center Link' URL based off Ticket 'ID'
df['Help Center Link'] = 'https://liferay-support.zendesk.com/agent/tickets/' + df['ID'].astype(str)


# Render Modified CSV to check if new columns correctly generated
print('---')
print('Modified DataFrame')
print(df.to_string())

# Generate new CSV file called test_formatted.csv
# in folder ./formatted/
# with index removed in utf-8 encoding
df.to_csv('./formatted/test_formatted.csv', index=False, encoding='utf-8')

# Next steps to consider:
# -- 
# Wildcard grab (all?) raw CSV file from a ./raw/ directory
# and auto-generate modified CSV into ./foramtted/ directory
# Reference: https://www.geeksforgeeks.org/how-to-read-all-csv-files-in-a-folder-in-pandas/
# --
# Or possibly make file name a variable that I can set either at the top or in .env
# such as if original file is /{var}.csv, the outputted would be /formatted/formatted_{var}.csv
