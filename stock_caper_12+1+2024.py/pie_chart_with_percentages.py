# import yfinance as yf
# import matplotlib.pyplot as plt
#
# # Define the list of stock symbols
# stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
#
# # Fetch historical data for the stocks
# data = yf.download(stocks, start="2023-01-01", end="2024-01-01")['Adj Close']
#
# # Calculate the portfolio percentages based on the latest data
# portfolio_percentages = data.iloc[-1] / data.iloc[-1].sum()
#
# print(portfolio_percentages)
#
#
# # Create a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(portfolio_percentages, labels=stocks, autopct='%1.1f%%', startangle=140)
# plt.title('Stock Portfolio Composition')
# plt.show()
#
#
#
# import yfinance as yf
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define the list of stock symbols
# stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
#
# # Fetch historical data for the stocks
# data = yf.download(stocks, start="2023-01-01", end="2024-01-01")['Adj Close']
#
# # Calculate the percentage change for each stock
# percentage_change = data.pct_change().iloc[-1] * 100
#
# # Clean the data by replacing NaN values with zeros and using absolute values
# percentage_change_cleaned = percentage_change.replace(np.nan, 0).abs()
#
# # Calculate the absolute values for each stock
# absolute_values = data.iloc[-1]
#
# # Create a pie chart with labels for percentage change and absolute values
# plt.figure(figsize=(12, 6))
# plt.pie(absolute_values, labels=[f"{stock}\n{change:.2f}%\n{value:.2f}" for stock, change, value in zip(absolute_values.index, percentage_change_cleaned, absolute_values)], autopct='%1.1f%%', startangle=140)
# plt.title('Stock Portfolio Composition with Percentage Change and Absolute Values')
# plt.show()
#
# print([f"{stock}\n{change:.2f}%\n{value:.2f}" for stock, change, value in zip(absolute_values.index, percentage_change_cleaned, absolute_values)]
#
#


import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import numpy as np


# Function to fetch historical stock data
# def fetch_stock_data(stocks, start_date, end_date):
#     data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
#     return data
#
#
# # Function to create an interactive pie chart with Plotly
# def create_pie_chart(data):
#     percentage_change = data.pct_change().iloc[-1] * 100
#     percentage_change_cleaned = percentage_change.replace(np.nan, 0).abs()
#
#     # Create a pie chart using Plotly Express
#     fig = px.pie(
#         names=percentage_change_cleaned.index,
#         values=percentage_change_cleaned,
#         labels=[f"{stock}: {change:.2f}%" for stock, change in
#                 zip(percentage_change_cleaned.index, percentage_change_cleaned)],
#         title='Stock Portfolio Composition in Percentage Change'
#     )
#
#     return fig
#
#
# # Streamlit app
# def main():
#     st.title("Stock Portfolio Analysis")
#
#     # Sidebar for user input
#     st.sidebar.header("User Input")
#     start_date = st.sidebar.text_input("Enter Start Date (YYYY-MM-DD)", "2023-01-01")
#     end_date = st.sidebar.text_input("Enter End Date (YYYY-MM-DD)", "2024-01-01")
#     stocks = st.sidebar.text_area("Enter Stock Symbols (comma-separated)", "AAPL, GOOGL, AMZN, MSFT, TSLA").split(", ")
#
#     # Fetch stock data
#     stock_data = fetch_stock_data(stocks, start_date, end_date)
#
#     # Display stock data
#     st.header("Stock Data")
#     st.dataframe(stock_data)
#
#     # Create and display the pie chart with Plotly
#     st.header("Portfolio Composition")
#     pie_chart = create_pie_chart(stock_data)
#     st.plotly_chart(pie_chart)
#
#
# if __name__ == "__main__":
#     main()
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to fetch historical stock data
def fetch_stock_data(stocks, start_date, end_date):
    data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
    return data

# Function to create a pie chart
def create_pie_chart(percentage_change_cleaned, absolute_values):
    # Create a pie chart
    fig, (ax1) = plt.subplots(1, figsize=(12, 6))

    ax1.pie(percentage_change_cleaned, labels=[f"{stock}: {change:.2f}%" for stock, change in zip(percentage_change_cleaned.index, percentage_change_cleaned)], autopct='%1.1f%%', startangle=140)
    ax1.set_title('Stock Portfolio Composition in Percentage Change')

    # ax2.pie(absolute_values, labels=[f"{stock}: {value:.2f}" for stock, value in zip(absolute_values.index, absolute_values)], autopct='%1.1f%%', startangle=140)
    # ax2.set_title('Stock Portfolio Composition in Absolute Values')

    return fig

# Streamlit app
def main():
    st.title("Stock Portfolio Analysis")

    # Sidebar for user input
    st.sidebar.header("User Input")
    start_date = st.sidebar.text_input("Enter Start Date (YYYY-MM-DD)", "2023-01-01")
    end_date = st.sidebar.text_input("Enter End Date (YYYY-MM-DD)", "2024-01-01")
    stocks = st.sidebar.text_area("Enter Stock Symbols (comma-separated)", "AAPL, GOOGL, AMZN, MSFT, TSLA").split(", ")

    # Fetch stock data
    stock_data = fetch_stock_data(stocks, start_date, end_date)

    # Display stock data
    st.header("Stock Data")
    st.dataframe(stock_data)

    # Calculate the percentage change and absolute values
    percentage_change = stock_data.pct_change().iloc[-1] * 100
    percentage_change_cleaned = percentage_change.replace(np.nan, 0).abs()
    absolute_values = stock_data.iloc[-1]




    # Create and display the pie chart
    st.header("Portfolio Composition")
    fig = create_pie_chart(percentage_change_cleaned, absolute_values)
    st.pyplot(fig)

if __name__ == "__main__":
    main()

















import yfinance as yf
import plotly.express as px

# List of stock symbols
stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]

# Fetch historical data for the stocks
data = yf.download(stocks, start="2023-01-01", end="2024-01-01")['Adj Close']

# Calculate the total value for each stock
total_values = data.iloc[-1]

# Create a pie chart using Plotly Express
fig = px.pie(values=total_values, names=total_values.index, title='Stock Portfolio Composition')

# Add labels and values to the hover text
fig.update_traces(hoverinfo='label+percent+value', textinfo='label+percent+value')

# Show the plot
fig.show()

# streamlit run  pie_chart_with_percentages.py