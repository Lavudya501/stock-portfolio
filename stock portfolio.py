import yfinance as yf

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'data': self.get_stock_data(symbol)}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['shares'] -= shares

    def get_stock_data(self, symbol):
        stock_data = yf.download(symbol, start='2020-01-01', end='2023-01-01')
        return stock_data['Adj Close']

    def track_portfolio_performance(self):
        total_portfolio_value = 0
        for symbol, data in self.portfolio.items():
            current_price = data['data'].iloc[-1]
            total_stock_value = current_price * data['shares']
            total_portfolio_value += total_stock_value
            print(f"{symbol}: {data['shares']} shares, Current Price: ${current_price:.2f}, Total Value: ${total_stock_value:.2f}")

        print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")


# Example usage:
tracker = StockPortfolioTracker()

while True:
    stock_symbol = input("Enter a stock symbol (or 'done' to finish): ").upper()
    
    if stock_symbol == 'DONE':
        break
    
    try:
        shares = int(input("Enter the number of shares: "))
        tracker.add_stock(stock_symbol, shares)
    except ValueError:
        print("Invalid input. Please enter a valid number of shares.")

# Track portfolio performance
tracker.track_portfolio_performance()
