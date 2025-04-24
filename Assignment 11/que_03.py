# After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
# were on vacation, you’re now in the market for a new vehicle. Your insurance didn’t cover
# the loss, so you want to make sure you get a good deal on your new car.
# Given a Series of car asking_prices and another Series of car fair_prices, determine which
# cars for sale are a good deal. In other words, identify cars whose asking price is less than
# their fair price.
# The result should be a list of integer indices corresponding to the good deals
# in asking_prices.

import pandas as pd

# Take input from user
n = int(input("Enter the number of cars: "))

print("Enter asking prices (space-separated):")
asking_input = list(map(float, input().split()))

print("Enter fair prices (space-separated):")
fair_input = list(map(float, input().split()))

# Validate input length
if len(asking_input) != n or len(fair_input) != n:
    print("Error: Number of prices entered does not match the number of cars.")
else:
    # Create pandas Series
    asking_prices = pd.Series(asking_input)
    fair_prices = pd.Series(fair_input)

    # Identify good deals
    good_deals = asking_prices < fair_prices
    good_deal_indices = list(good_deals[good_deals].index)

    # Output
    print("Indices of good deals:", good_deal_indices)