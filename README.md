# Crypto-Portfolio-Tracker

# Cryptocurrency Portfolio Tracker

## Project Overview  
The **Cryptocurrency Portfolio Tracker** is a Python-based program designed to calculate the total value of a cryptocurrency portfolio using live prices from the **public CoinGecko API**. Users can input their cryptocurrency holdings (e.g., Bitcoin, Ethereum), and the program fetches real-time prices to provide a detailed value breakdown. Additionally, the program generates clear and insightful **visualizations** in the form of a **pie chart** and a **bar chart** to display portfolio composition.

---

## Project Purpose and Functionality  
The goal of this project is to:  
1. Provide a real-time value of a cryptocurrency portfolio based on user-defined holdings.  
2. Utilize the **CoinGecko API** for live price data without requiring an API key.  
3. Display data visualizations to help users analyze the distribution of their holdings.

### Key Features:
- Fetches live cryptocurrency prices from the public CoinGecko API.  
- Calculates the total portfolio value and provides a breakdown by cryptocurrency.  
- Generates:
   - **Pie Chart**: Shows the percentage contribution of each cryptocurrency.  
   - **Bar Chart**: Displays the absolute value of holdings in USD.  

---

## Installation Instructions  

### Prerequisites  
- **Python 3.x**  
- Required Libraries:
  - `requests` - For fetching data from the API.  
  - `matplotlib` - For generating visualizations.  

---

### Steps to Install and Run the Project  

1. **Clone the Repository**  
   Open your terminal and clone the project from GitHub:  
   `git clone https://github.com/yourusername/crypto_portfolio_tracker.git`
   `cd crypto_portfolio_tracker`
2. **Install Dependencies**
Install the required libraries using pip:
  `pip install requests matplotlib`
3. **Run the Project**
Execute the main.py file to run the program:
  `python3 main.py`
4. **View the Outputs**
  * The program will display the total portfolio value and a breakdown in the terminal.
  * It will also generate:
    - A pie chart showing the portfolio distribution.
    - A bar chart showing the absolute value of each cryptocurrency.

### API Details
The project uses the CoinGecko API to fetch real-time cryptocurrency prices. This API is public and does not require an API key.

* API Endpoint: `https://api.coingecko.com/api/v3/simple/price`
* Parameters:
    ids: A list of cryptocurrency IDs (e.g., "bitcoin, ethereum").
    vs_currencies: The currency to display prices in (default: "usd").  

### Notes
- The CoinGecko API is public, so no API key is required to run this project.
- Ensure you have a stable internet connection while running the program
