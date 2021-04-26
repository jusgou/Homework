"""
Conditionally Yours

Pseudocode:


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price

original_price = 360.35

# Create integer variable for current_price
current_price = 293.33

# Create float for threshold_to_buy
threshold_to_buy = -10.00

# Create float for threshold_to_sell
threshold_to_sell = 20.00

# Create float for portfolio balance

# Create float for balance check


# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price is ${current_price}")
      

# Print percent increase
print(f"Netflix's changed by {percent_increase:.2f}%")

# Determine if stock should be bought or sold
if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
elif percent_increase < threshold_to_sell and percent_increase > threshold_to_buy:
    recommedation = "hold"
else:
    print("Not enough data to make a decision. Need human input") 

# Print recommendation
print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance variable as a float
balance = 5000.00

# Declare balance_check variable
balance_check = balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${balance} in excess equity available in your portfolio.")

if recommendation == "buy" and balance_check > current_price:
    print("Final Recommedation: " + recommendation)
elif recommendation == "buy" and balance_check < current_price:
    print("Final recommendation: You should buy. But you don't have enough available capital.")
else: 
    print("Final Recommedation: " + recommendation)

# IF-ELSE Logic to determine recommendation based off of balance check
