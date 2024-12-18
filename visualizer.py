# Creating the Visualization Class to generate pie and bar charts

# Pie Chart:

import matplotlib.pyplot as plt

class Visualizer:
    """Generates visualizations for portfolio analysis."""

    @staticmethod
    def plot_pie_chart(portfolio_breakdown):
        """
        Generates a pie chart for portfolio breakdown.
        Args:
            portfolio_breakdown (dict): Breakdown of portfolio values by cryptocurrency.
        """
        labels = list(portfolio_breakdown.keys())  # Get crypto names
        sizes = list(portfolio_breakdown.values())  # Get corresponding values
        plt.figure(figsize=(8, 8))  # Set figure size
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)  # Create pie chart
        plt.title("Cryptocurrency Portfolio Breakdown")  # Set chart title
        plt.show()  # Display the chart

        
    # Bar Chart:
    
    @staticmethod
    def plot_bar_chart(portfolio_breakdown):
        """
        Generates a bar chart for portfolio values.
        Args:
            portfolio_breakdown (dict): Breakdown of portfolio values by cryptocurrency.
        """
        labels = list(portfolio_breakdown.keys())  # Get crypto names
        sizes = list(portfolio_breakdown.values())  # Get corresponding values
        plt.figure(figsize=(10, 6))  # Set figure size
        plt.bar(labels, sizes, color="skyblue")  # Create bar chart
        plt.xlabel("Cryptocurrencies")  # X-axis label
        plt.ylabel("Portfolio Value (USD)")  # Y-axis label
        plt.title("Cryptocurrency Portfolio Values")  # Chart title
        plt.show()  # Display the chart
        