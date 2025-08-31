
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

# Take user input for stock names and quantity
n = int(input("Enter number of different stocks you own: "))
for _ in range(n):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
        total_investment += stock_prices[stock_name] * quantity
    else:
        print(f"{stock_name} not found in stock price list.")

# Display total investment
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each")
print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Your Portfolio:\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")
print("\nPortfolio saved to portfolio.txt")