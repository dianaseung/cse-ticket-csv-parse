import pandas as pd
import numpy as np

# Import the CVS from custom 'All My Tickets View'
df = pd.read_csv('test.csv',
    parse_dates=['Requested','Updated'])

