# Importing library

import requests

# Creating a Class for Fetching Cryptocurrency Prices

class CryptoPortfolioTracker:
    # Tracks cryptocurrency portfolio and calculates values.

    def __init__(self):
        # Base URL for the CoinGecko API
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"

    def fetch_crypto_prices(self, cryptos, vs_currency="usd"):
        """ Fetches real-time prices for a list of cryptocurrencies.
        Args:
            cryptos (list): List of cryptocurrency names (e.g., ['bitcoin', 'ethereum']).
            vs_currency (str): The currency in which prices are fetched (default is USD).
        Returns:
            dict: A dictionary containing prices for each cryptocurrency."""
        ids = ",".join(cryptos)  # Convert list of cryptos to a comma-separated string
        params = {
            "ids": ids,  # Pass the cryptocurrency IDs
            "vs_currencies": vs_currency,  # Specify the currency (e.g., USD)
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()  # Return the price data as a dictionary
        else:
            # Raise an exception if the API call fails
            raise Exception("Failed to fetch cryptocurrency prices.")

    
    # Calculate the total portfolio value and and providing a breakdown by cryptocurrency

    def calculate_portfolio_value(self, holdings, prices):
        """
        Calculates the total portfolio value based on holdings and prices.
        Args:
            holdings (dict): Dictionary of holdings with crypto names as keys and amounts as values.
            prices (dict): Dictionary of real-time prices fetched from the API.
        Returns:
            tuple: Total portfolio value and a breakdown by cryptocurrency.
        """
        portfolio_value = 0  # Initialize total portfolio value
        portfolio_breakdown = {}  # Dictionary to store value per cryptocurrency
        for crypto, amount in holdings.items():
            if crypto in prices:
                value = amount * prices[crypto]["usd"]  # Calculate value for each cryptocurrency
                portfolio_value += value  # Add to total portfolio value
                portfolio_breakdown[crypto] = value  # Store the value in breakdown
        return portfolio_value, portfolio_breakdown

