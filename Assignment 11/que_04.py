# Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.

import pandas as pd
import numpy as np

data = {
    'John': [True, False, True, False, True, True, False, False, True, False],
    'Judy': [True, False, False, False, True, False, True, False, True, True]
}

df = pd.DataFrame(data)
df['party'] = df['John'] & df['Judy']
party_days = df.index[df['party']].tolist()
days_til_party = []

for i in range(len(df)):
    future_parties = [day - i for day in party_days if day >= i]
    if future_parties:
        days_til_party.append(future_parties[0])
    else:
        days_til_party.append(-1)

df['days_til_party'] = days_til_party
df.drop(columns='party', inplace=True)
print(df)