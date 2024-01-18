import yfinance as yf
import plotly.express as px
import pandas as pd
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
# fig.show()






import yfinance as yf
import plotly.express as px

# Replace these with the symbols of the stocks you're interested in
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

data = yf.download(symbols, start='2023-01-01', end='2024-01-01')['Adj Close']

# Calculate the percentage change
percentage_change = data.pct_change().mean() * 100

# Calculate the current values
current_values = data.iloc[-1]

# Create a DataFrame for plotly express
df = pd.DataFrame({'Symbols': symbols, 'Values': current_values, 'Change Percentage': percentage_change})

# Select the top 20 values based on 'Values'
df_top20 = df.nlargest(20, 'Values')

# Plotting
fig = px.pie(df_top20, values='Values', names='Symbols',
             hover_data=['Symbols', 'Change Percentage'],
             labels={'Symbols': 'Stock Symbol', 'Values': 'Value', 'Change Percentage': 'Change Percentage'},
             title="Top 20 Stock Portfolio Overview")

# Add labels and values to the hover text
fig.update_traces(hoverinfo='label+percent+value', textinfo='label+percent+value')

# Display the figure
fig.show()
