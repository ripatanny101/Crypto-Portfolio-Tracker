# Main Program Execution (allow the user to input their portfolio and visualize the results)

if __name__ == "__main__":
    try:
        # Example cryptocurrency holdings defined by the user
        holdings = {
            "bitcoin": 0.5,  # 0.5 BTC
            "ethereum": 10,   # 10 ETH
            "dogecoin": 8000  # 8000 DOGE
        }

        # Instantiate the tracker and fetch prices
        tracker = CryptoPortfolioTracker()
        cryptos = list(holdings.keys())  # Extract the list of cryptocurrencies from holdings
        prices = tracker.fetch_crypto_prices(cryptos)  # Fetch real-time prices from API

        # Calculate the total portfolio value and breakdown
        total_value, breakdown = tracker.calculate_portfolio_value(holdings, prices)
        print(f"Total Portfolio Value: ${total_value:,.2f}")  # Display total portfolio value
        for crypto, value in breakdown.items():
            print(f"{crypto.capitalize()}: ${value:,.2f}")  # Display value for each cryptocurrency

        # Visualize the portfolio with multiple charts
        visualizer = Visualizer()
        visualizer.plot_pie_chart(breakdown)  # Generate a pie chart
        visualizer.plot_bar_chart(breakdown)  # Generate a bar chart

    except Exception as e:
        # Handle any errors that occur
        print(f"An error occurred: {e}")
