import pandas as pd

df = pd.read_csv('https://d3ejq4mxgimsmf.cloudfront.net/india_census_2011-ce94dcde69614e2686012fcff798c587.csv')

# compute literacy rate per district
df['literacy_rate'] = df['Literate'] / df['Population']

# get index of max literacy per state
idx = df.groupby('State name')['literacy_rate'].idxmax()

print(idx)

# build correct Series: State -> District name
ser_out = df.loc[idx].set_index('State name')['District name']

# DO NOT CHANGE THIS LINE
print(ser_out[input().strip()])