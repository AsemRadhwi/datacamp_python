# Import pandas 
import pandas as pd
import numpy as np

# Use pandas to read in recent_grads_url
recent_grads_url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_6060/datasets/recent_grads.csv'
recent_grads = pd.read_csv(recent_grads_url)

# Print the shape
print(recent_grads.shape)

# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())

# Exclude data of type object
print(recent_grads.describe(exclude=['object']))

# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan

# Select sharewomen column
sw_col = recent_grads['sharewomen']

# Output first five rows
print(sw_col.head(5))

# Import numpy
import numpy as np

# Use max to output maximum values
max_sw = np.max(sw_col)

# Print column max
print(max_sw)

# Output the row containing the maximum percentage of women
print(recent_grads[sw_col==max_sw])

# Convert to numpy array
recent_grads_np = np.array(recent_grads[['unemployed', 'low_wage_jobs']])


# Print the type of recent_grads_np
print(type(recent_grads_np))

# Calculate correlation matrix
print(np.corrcoef(recent_grads_np[:,0], recent_grads_np[:,1]))

# Add sharemen column
recent_grads['sharemen'] = recent_grads['men'] / recent_grads['total']

# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])
 
# Output the row with the highest percentage of men
print(recent_grads[recent_grads['sharemen']==max_men])

# Add gender_diff column
recent_grads['gender_diff'] = recent_grads['sharewomen'] - recent_grads['sharemen'] 

# Make all gender difference values positive
recent_grads['gender_diff'] = recent_grads['gender_diff'].abs()

# Find the 5 rows with lowest gender rate difference
print(recent_grads.nsmallest(5, 'gender_diff'))

# Rows where gender rate difference is greater than .30 
diff_30 = recent_grads['gender_diff'] > .30

# Rows with more men
more_men = recent_grads['men'] > recent_grads['women']

# Combine more_men and diff_30
more_men_and_diff_30 = np.logical_and(diff_30,more_men)

# Find rows with more men and and gender rate difference greater than .30
fewer_women = recent_grads[more_men_and_diff_30]

# Group by major category and count
print(recent_grads.groupby(['major_category']).major_category.count())

# Group departments that have less women by category and count
print(fewer_women.groupby('major_category').major_category.count())

# Report average gender difference by major category
print(recent_grads.groupby('major_category').gender_diff.mean())

# Find average number of low wage jobs and unemployment rate of each major category
dept_stats = recent_grads.groupby(['major_category'])['low_wage_jobs', 'unemployment_rate'].mean()
print(dept_stats)