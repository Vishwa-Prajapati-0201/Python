# Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.

import pandas as pd

# Sample dataset
concerts = pd.DataFrame({
    'artist': ['A', 'A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'venue': ['X', 'Y', 'X', 'X', 'Z', 'Z', 'Y', 'Y'],
    'date': pd.to_datetime([
        '2025-01-15', '2025-01-20', '2025-01-15', '2025-02-10',
        '2025-01-25', '2025-02-15', '2025-02-18', '2025-02-22'
    ])
})

# Extract year-month
concerts['year_month'] = concerts['date'].dt.to_period('M').astype(str)

# Create artist-venue pairs
artists = concerts['artist'].unique()
venues = concerts['venue'].unique()
year_months = concerts['year_month'].unique()

# Create all combinations manually using a DataFrame merge
all_combos = pd.DataFrame({'year_month': year_months}).merge(
    pd.DataFrame({'artist': artists}), how='cross'
).merge(
    pd.DataFrame({'venue': venues}), how='cross'
)

# Count actual concerts
grouped = concerts.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

# Merge with all combos and fill missing counts with 0
merged = all_combos.merge(grouped, on=['year_month', 'artist', 'venue'], how='left').fillna(0)

# Pivot to wide format
wide = merged.pivot(index='year_month', columns=['artist', 'venue'], values='count')

# Flatten column names
wide.columns = [f'{a}_{v}' for a, v in wide.columns]
wide = wide.reset_index()

print(wide)


"""concerts = pd.DataFrame({
    'artist': ['X', 'Y', 'X', 'Z', 'Y', 'Y', 'X', 'Z', 'Z'],
    'venue': ['A', 'B', 'B', 'A', 'A', 'C', 'A', 'C', 'B'],
    'date': pd.to_datetime([
        '2025-03-05', '2025-03-10', '2025-03-15', '2025-03-18',
        '2025-04-01', '2025-04-05', '2025-04-08', '2025-04-12', '2025-04-20'
    ])
}) """