import yfinance as yf
import plotly.express as px
import pandas as pd

from urllib.request import urlopen
from urllib.error import HTTPError
from nsetools import Nse
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_nse_sector_data():
    url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"

    # Use a different user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first table on the page
        table = soup.find('table')

        if table:
            # Extract data from the table
            data = []
            for row in table.find_all('tr')[1:]:
                cols = row.find_all(['td', 'th'])
                cols = [col.text.strip() for col in cols]
                data.append(cols)

            # Create a DataFrame
            df = pd.DataFrame(data,
                              columns=['Symbol', 'Company Name', 'Last Price', 'Change', 'Percentage Change', 'Open',
                                       'High', 'Low', '52-Week High', '52-Week Low', 'Volume', 'Market Cap'])

            # Save the DataFrame to an Excel file
            df.to_excel('nse_sector_list.xlsx', index=False)
            print("Data saved to 'nse_sector_list.xlsx'")
        else:
            print("Error: Table not found on the page")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_nse_sector_data()

# Replace these with the symbols of the stocks you're interested in
symbols = ['ABB.BO', 'ABBOTINDIA.BO', 'ABCAPITAL.BO', 'ADANIPORTS.BO',
           'ADANIPOWER.BO', 'ALKEM.BO', 'APOLLOHOSP.BO', 'APOLLOTYRE.BO',
           'ASHOKLEY.BO', 'ASIANPAINT.BO',
           # ... Add all your symbols here
           'TVSMOTOR.BO', 'UBL.BO', 'ULTRACEMCO.BO', 'UNIONBANK.BO', 'VBL.BO',
           'VEDL.BO', 'VOLTAS.BO', 'WIPRO.BO', 'ZOMATO.BO', 'ZYDUSLIFE.BO']

data = yf.download(symbols, start='2023-01-01', end='2024-01-01')['Adj Close']

# Calculate the percentage change for each stock individually
percentage_change = data.pct_change().mean(axis=0) * 100

# Calculate the current values
current_values = data.iloc[-1]

# Create a DataFrame for plotly express
df = pd.DataFrame({'Symbols': symbols, 'Values': current_values, 'Change Percentage': percentage_change})

# Select the top 20 values based on 'Values'
df_top20 = df.nlargest(15, 'Values').round(2)
# Round numbers to two decimal places in the text information
df_top20['Values'] = df_top20['Values'].round(2)
df_top20['Change Percentage'] = df_top20['Change Percentage'].round(2)


# Plotting
fig = px.pie(df_top20, values='Values', names='Symbols',
             hover_data=['Symbols', 'Change Percentage'],
             labels={'Symbols': 'Stock Symbol', 'Values': 'Value', 'Change Percentage': 'Change Percentage'},
             title="Top 20 Stock Portfolio Overview")

# Add labels and values to the hover text
fig.update_traces(hoverinfo='label+percent+value', textinfo='label+percent+value')

# Display the figure
fig.show()
