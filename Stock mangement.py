# Stock Mangement
!pip install yfinance pandas
#fetch stck data
import yfinance as yf

def get_stock_price(symbol):
    """Fetches the current stock price for a given symbol."""
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")['Close'].iloc[-1]
    #portfolio mangement
portfolio = {}

def add_stock(symbol, shares):
    """Adds a stock to the portfolio."""
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol} to the portfolio.")

def remove_stock(symbol, shares):
    """Removes a stock from the portfolio."""
    if symbol in portfolio:
        if portfolio[symbol] >= shares:
            portfolio[symbol] -= shares
            if portfolio[symbol] == 0:
                del portfolio[symbol]
            print(f"Removed {shares} shares of {symbol} from the portfolio.")
        else:
            print("Not enough shares to remove.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    """Displays the current portfolio and its value."""
    total_value = 0
    print("Current Portfolio:")
    for symbol, shares in portfolio.items():
        price = get_stock_price(symbol)
        value = price * shares
        total_value += value
        print(f"{symbol}: {shares} shares at ${price:.2f} each, Total: ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")
    #user inteface

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(symbol, shares)
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# The second definition of main, get_stock_price, add_stock, remove_stock and view_portfolio have been removed because they are duplicates.
# The while loop and following logic within the second main function was already present in the first,
# and the redundant function definitions were likely causing confusion.


if __name__ == "__main__":
    main()
