import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol):
        if symbol.upper() not in self.portfolio:
            self.portfolio[symbol.upper()] = yf.Ticker(symbol.upper())

    def remove_stock(self, symbol):
        if symbol.upper() in self.portfolio:
            del self.portfolio[symbol.upper()]
        else:
            print("Stock not found in portfolio.")

    def get_portfolio_data(self):
        data = {}
        for symbol, stock in self.portfolio.items():
            data[symbol] = stock.history(period="1d")["Close"].iloc[-1]
        return data

    def get_portfolio_value(self):
        data = self.get_portfolio_data()
        return sum(data.values())

    def track_performance(self):
        data = self.get_portfolio_data()
        print("Current Portfolio:")
        for symbol, price in data.items():
            print(f"{symbol}: ${price:.2f}")

        portfolio_value = self.get_portfolio_value()
        print(f"Total Portfolio Value: ${portfolio_value:.2f}")

# Example Usage
portfolio = StockPortfolio()

while True:
    see_stocks = input("Do you want to see your stocks? (Yes/No): ").strip().lower()
    if see_stocks == 'yes':
        portfolio.track_performance()
        add_stock_choice = input("Do you want to add a stock? (Yes/No): ").strip().lower()
        if add_stock_choice == 'yes':
            symbol = input("Enter the stock symbol to add: ")
            portfolio.add_stock(symbol)
            portfolio.track_performance()
            print("Total Portfolio Value:", portfolio.get_portfolio_value())
    elif see_stocks == 'no':
        while True:
            action = input("Do you want to (A)dd or (R)emove a stock? (Q)uit: ").upper()
            if action == 'A':
                symbol = input("Enter the stock symbol to add: ")
                portfolio.add_stock(symbol)
                portfolio.track_performance()
                print("Total Portfolio Value:", portfolio.get_portfolio_value())
            elif action == 'R':
                symbol = input("Enter the stock symbol to remove: ")
                portfolio.remove_stock(symbol)
                portfolio.track_performance()
                print("Total Portfolio Value:", portfolio.get_portfolio_value())
            elif action == 'Q':
                print("Okay!")
                break
            else:
                print("Invalid option. Please choose A, R, or Q.")
    else:
        print("Invalid input. Please enter Yes or No.")
        continue
        
    quit_prompt = input("Do you want to quit? (Yes/No): ").strip().lower()
    if quit_prompt == 'yes':
        print("Come Again!")
        break
    else:
        portfolio.track_performance()
        print("Total Portfolio Value:", portfolio.get_portfolio_value())
