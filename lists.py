# Define the hairstyles and prices lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Define the last_week list
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the total price of all haircuts
total_price = 0
for price in prices:
    total_price += price

# Calculate the average price of haircuts
average_price = total_price / len(prices)

# Print the average haircut price
print(f'Average Haircut Price: {average_price}')

# Create a new list with discounted prices
new_prices = [price - 5 for price in prices]

# Print the new prices list
print(new_prices)

# Calculate the total revenue generated from haircuts
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

# Print the total revenue
print(total_revenue)

# Calculate the average daily revenue
average_daily_revenue = total_revenue / 7

# Print the average daily revenue
print(average_daily_revenue)

# Create a list of haircuts priced under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Print the list of haircuts under 30 dollars
print(cuts_under_30)

# The code calculates the average haircut price, creates a new list with discounted prices, calculates the total revenue generated 
# from haircuts, calculates the average daily revenue, and finally creates a list of haircuts priced under 30 dollars. The results
#  are printed for each calculation.