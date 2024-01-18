


import os
#
# try:
#     import xlwings
# except ImportError:
#     os.system('python -m pip install --upgrade pip')
#openpyxl

# try:
#     import openpyxl
# except ImportError:
#     os.system('python -m pip install openpyxl')


# try:
#     import xlwings
# except ImportError:
#     os.system('python -m pip install xlwings==0.30.12')
# try:
#     import pandas
# except ImportError:
#     os.system('python -m pip install pandas')
#
#
# try:
#     import yfinance
# except ImportError:
#     os.system('python -m pip install yfinance==0.2.28')
# try:
#     import tabulate
# except ImportError:
#     os.system('python -m pip install tabulate')
#
#
# try:
#     import pyotp
# except ImportError:
#     os.system('python -m pip install pyotp')


# try:
#     import streamlit
# except ImportError:
#     os.system('python -m pip install streamlit')
#
#

# try:
#     import plotly
# except ImportError:
#     os.system('python -m pip install plotly')
# try:
#     import treamlit_option_menu
# except ImportError:
#     os.system('python -m pip install streamlit-option-menu')
# try:
#     import streamlit_extras
# except ImportError:
#     os.system('python -m pip install streamlit_extras')


import streamlit as st
from datetime import date

import yfinance as yf
#
# from prophet.plot import plot_plotly
# from plotly import graph_objects as go
#
# from prophet import Prophet
import pandas as pd

# streamlit run tt.py
import xlwings
import streamlit as st  #  pip install streamlit
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu

from streamlit_extras.metric_cards import style_metric_cards
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

st.title('LIT FINANCE DASHBOARD')


def tickers_add_BO_NS(tickers, EXCHANGE):
    count = 0
    # print("symbol", tickers)
    for tickers_list1 in tickers:
        tickers[count] = str(f"{tickers_list1}.{EXCHANGE}")
        count = count + 1
    # print(tickers)
    return tickers


data1 = pd.read_csv("NIFTY 50.csv")
data2 = list(data1["NIFTY 20"].values)
data3 = list(data1["NIFTY 50"].values)
data4 = list(data1["NIFTY NEXT 50"].values)
data5 = list(data1["NIFTY 200"].values)
data6 = list(data1["NIFTY MIDCAP 50"].values)
data7 = list(data1["NIFTY MIDCAP 100"].values)
data8 = list(data1["NIFTY MIDSMALLCAP 400"].values)
data9 = list(data1["NIFTY TOTAL MARKET"][:].values)

stock_INDEX = ["NIFTY 200","NIFTY 20","NIFTY 50","NIFTY NEXT 50","NIFTY 200",
              "NIFTY MIDCAP 50","NIFTY MIDCAP 100","NIFTY MIDSMALLCAP 400","NIFTY MIDSMALLCAP 400","NIFTY TOTAL MARKET"]


NSE1 = pd.read_csv("NSE.csv")

print(NSE1)
breakpoint()
# selected_stock_INDEX = st.selectbox('selected dataset for  INDEX',stock_INDEX)
# EXCHANGE ={"BSE":'BO',"NSE":'NS' }
# tickers = list(data1[selected_stock_INDEX].values)
# selected_stock_EXCHANGE = st.selectbox('selected dataset for  EXCHANGE',['BSE','NSE'])
# data_tickers = tickers_add_BO_NS(tickers=tickers, EXCHANGE=EXCHANGE[selected_stock_EXCHANGE])


# # stocks = ('RELI','TCS.BO','WIT','INFY')
# stock_tickers = st.selectbox('selected dataset for predicction',data_tickers)
#
# print(stock_tickers)






# streamlit run tt.py

# stocks = ('RELI','TCS.BO','WIT','INFY')
# dropdown = st.multiselect('pick your assets',stocks)
#
#
# start = st.date_input('Start Date',value=pd.to_datetime('2021-01-01'))
# end = st.date_input('End Date',value=pd.to_datetime('today'))
#


def stock_parsent(df):
     rel = df.pct_change()
     cumret = ((1+rel).cumprod() - 1) * 100
     cumret = cumret.fillna(0)
     return  cumret


# if len(dropdown) > 0:
#     # df = yf.download(dropdown,start,end)['Adj Close']
#     # df = stock_parsent(yf.download(data_tickers,start,end))['Adj Close']
#     df = yf.download(data_tickers, start, end)['Adj Close']
#     df.sort_values('Date', inplace=False)
#     st.title('STOCK LPT')
#     st.write(df)
#     print(df)
#     percentage = ((df-df.shift(1)) / df.shift(1)) * 100
#
#     percentage_cumsum = percentage.cumsum(axis='rows')  # df.cumsum(axis='columns')
#
#     st.title('STOCK percentage ')
#     st.write(percentage_cumsum)
#     # percentage_cumsum = percentage_cumsum1.transpose()
#     st.title(selected_stock_INDEX)
#     st.line_chart(percentage_cumsum)

# df = stock_parsent(yf.download(stocks,start,end))['Adj Close']
# print(df)


# with st.sidebar:
#     selected = option_menu("Options Menu", ['Third', "Fourth"],
#                            icons=['play', 'play'], menu_icon="cast", default_index=1)
#
#     if selected == "Third":
#         textInput_4 = st.text_input(
#             "First input", value='default 4', key='4')
#         textInput_5 = st.text_input(
#             "Second input", value='default 5', key='5')
#         st.write(bool(textInput_4))
#         if not textInput_4 or not textInput_5:
#             st.sidebar.info("Add input in sidebar")
#     elif selected == "Fourth":
#         textInput_6 = st.text_input("Third input", value='default 6', key='6')
#         if not textInput_6:
#             st.sidebar.info("Add input in sidebar")





def Equity_Options_BOKREJ_pie(pie_df,symbol,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = pie_df_data['Profit'].sum()
    pie_df = pd.DataFrame(pie_df_data)
    pie_df['Profit'] = pie_df['Profit'].abs()
    Profit_pie = pie_df.loc[pie_df['Profit'] >= 0]
    print("  Profit_pie 329",  Profit_pie)

    def colors_(df):
        if df > 0:
            colors_ ='green'             #facecolor  '#333333'
        else:
            colors_ = 'red'
        return colors_
    # print(pie_df_data)

    custom_colors = {'Holding': colors_(df=pie_df_data['Profit'][0]),  'Intraday': colors_(df=pie_df_data['Profit'][1]),
                     'Options': colors_(df=pie_df_data['Profit'][2]),  'Charges': 'red',
                     'Charges debit': colors_(df=pie_df_data['Profit'][4]), "Dividends": 'green'}

    fig = px.pie(Profit_pie, values='Profit', names='symbol', color='symbol', #color_discrete_map=custom_colors,
                 title=f"ALL DATA piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Profit value', legend_y=0.9, paper_bgcolor='#80aaff', width=width, height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))

    return fig






width = 2000
height = 625
Book_NAME = "data_NSC_ALL2.xlsx"

def exl_sheets_clear(sheets_name):
    ws = xlwings.Book(Book_NAME).sheets(sheets_name)
    ws.clear()


def exl_sheets_list(exl_sheets_list):
    for i in exl_sheets_list:
        exl_sheets_clear(sheets_name=i)




def print_sheets(df, sheets_name, range):
    ws = xlwings.Book(Book_NAME).sheets(sheets_name)
    ws.range(range).value = pd.DataFrame(df.round(2))




def yfinance_download(tickers_list, start_date, end_date,interval):
    yfinance_download = yf.download(tickers_list, start_date, end_date, interval=interval)['Adj Close']
    yfinance_download = yfinance_download.fillna(method='ffill', axis=0)
    yfinance_download = yfinance_download.fillna(method='bfill')
    # print(yfinance_download)
    yfinance_download.index.name = 'Date'
    yfinance_download['Date'] = pd.to_datetime(yfinance_download.index)
    yfinance_download.set_index('Date', inplace=True)
    yfinance_download.index = yfinance_download.index.strftime('%d-%m-%Y- %H:%M:%S')
    print_sheets(df=yfinance_download, sheets_name="Adj Close", range="A1")
    return yfinance_download


def live_market_df(DATE,df):
    yfinance_download_transpose = df
    live_market = pd.DataFrame()
    #
    #
    # print(DATE)
    # print(DATE[0],len(DATE)-1)
    DATE_start= DATE[0]
    DATE = DATE[len(DATE)-1]
    index = yfinance_download_transpose.columns.get_loc(DATE)
    live_market["DATE_start"] = DATE_start
    live_market = pd.DataFrame(live_market["DATE_start"])

    live_market["opne"] = yfinance_download_transpose.iloc[:, 0]

    live_market["DATE_END"] = DATE
    live_market["Close"] = yfinance_download_transpose.iloc[:, index]
    # live_market["high"] = yfinance_download_high_transpose.iloc[:, index]
    live_market["PARSENT"] = (yfinance_download_transpose.iloc[:,index] - yfinance_download_transpose.
                              iloc[:,0]) / yfinance_download_transpose.iloc[:,0] * 100


    #
    # live_market["PARSENT_high%"] = (yfinance_download_high_transpose.iloc[:,index] - yfinance_download_high_transpose.iloc[:,
    #                                 0]) / yfinance_download_high_transpose.iloc[:, 0] * 100
    live_market["CHANGE"] = yfinance_download_transpose.iloc[:, index] - yfinance_download_transpose.iloc[:, 0]
    live_market["Rank_PARSENT"] = live_market["PARSENT"].rank(ascending=0)
    # live_market["Rank_high"] = live_market["PARSENT_high%"].rank(ascending=0)
    live_market["DATE_start"] = DATE_start

    live_market.index.name = 'symbol'

    # if strategy == "Rank_high":
    #     live_market.sort_values("Rank_high", axis=0, ascending=True, inplace=True)
    # else:
    live_market.sort_values("Rank_PARSENT", axis=0, ascending=True, inplace=True)
    return live_market





sheets_list = ["NSE", "holdings", "orders", "Adj Close", "Volume",
               "HIGH", "upper_circuit_count"]
exl_sheets_list(exl_sheets_list=sheets_list)

def run():
        # selected_stock_INDEX = st.sidebar.selectbox('selected dataset for  INDEX', stock_INDEX)
        # EXCHANGE = {"BSE": 'BO', "NSE": 'NS'}
        # tickers = list(data1[selected_stock_INDEX].values)
        # selected_stock_EXCHANGE = st.sidebar.selectbox('selected dataset for  EXCHANGE', ['BSE', 'NSE'])
        # data_tickers = tickers_add_BO_NS(tickers=tickers, EXCHANGE=EXCHANGE[selected_stock_EXCHANGE])
        #
        # start = st.sidebar.date_input('Start Date', value=pd.to_datetime('2023-01-01'))
        # end = st.sidebar.date_input('End Date', value=pd.to_datetime('today'))
        # top_20 = st.number_input(" top_20", value=15, key='top_20')

    # all_qttar_dict_list = uploaded_file2(all_qttar_dict=all_qttar_dict, key="key2")
        st.sidebar.image("IMG_20190423_172859.png",
                         caption="Developed and   application problem solving   by: KUKAN MANOJ    : helpline   number -> 9106963281")
        # print("all_qttar_dict_list lin 173 ", time_())
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home', 'your uploaded_file', 'Add Your Capital', 'Holding', 'Intraday', 'Options', 'Charges',
                         'Charges Debits and Credits', 'Dividends', 'Settings', 'about'],
                #           https: // icons.getbootstrap.com /  # icons     'person-circle'

                icons=['house-fill', 'journal-arrow-up', 'journal-arrow-up', 'trophy-fill', 'apple', 'play-btn-fill',
                       'caret-right-square-fill', 'caret-right-square-fill', 'caret-right-square-fill', 'gear',
                       'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "30px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"}, })

            # print("option_menu lin 189 ", time_())
        if app == "Home":

            selected_stock_INDEX = st.sidebar.selectbox('selected dataset for  INDEX', stock_INDEX)
            EXCHANGE = {"BSE": 'BO', "NSE": 'NS'}
            tickers = list(data1[selected_stock_INDEX].values)
            selected_stock_EXCHANGE = st.sidebar.selectbox('selected dataset for  EXCHANGE', ['BSE', 'NSE'])
            data_tickers = tickers_add_BO_NS(tickers=tickers, EXCHANGE=EXCHANGE[selected_stock_EXCHANGE])

            start = st.sidebar.date_input('Start Date', value=pd.to_datetime('2023-01-01'))
            end = st.sidebar.date_input('End Date', value=pd.to_datetime('today'))
            top_20 = st.number_input( " top_20", value=15, key='top_20')

            import yfinance as yf
            import plotly.express as px


            # Replace these with the symbols of the stocks you're interested in
            symbols = ['ABB.BO', 'ABBOTINDIA.BO', 'ABCAPITAL.BO', 'ADANIPORTS.BO',
                       'ADANIPOWER.BO', 'ALKEM.BO', 'APOLLOHOSP.BO', 'APOLLOTYRE.BO',
                       'ASHOKLEY.BO', 'ASIANPAINT.BO',
                       # ... Add all your symbols here
                       'TVSMOTOR.BO', 'UBL.BO', 'ULTRACEMCO.BO', 'UNIONBANK.BO', 'VBL.BO',
                       'VEDL.BO', 'VOLTAS.BO', 'WIPRO.BO', 'ZOMATO.BO', 'ZYDUSLIFE.BO']

            # data = yf.download(symbols, start='2023-01-01', end='2024-01-01')['Adj Close']

            yfinance_download1 = yfinance_download(tickers_list=data_tickers, start_date=start, end_date=end,interval="1d")
            yfinance_download_transpose = yfinance_download1.transpose()
            DATE_list = pd.DataFrame(yfinance_download1.index)


            live_market_data = live_market_df(DATE=DATE_list["Date"],df=yfinance_download_transpose)

            live_market_data =  live_market_data.loc[live_market_data['PARSENT'] >= 0]

            live_market_data = pd.DataFrame(live_market_data).head( top_20)




            print_sheets(df=live_market_data, sheets_name="NSE", range="A1")


            fig = px.pie(live_market_data, values='PARSENT', names=live_market_data.index,# color=live_market_data.index,
                         # color_discrete_map=custom_colors,
                         title=f"ALL DATA piy chaty = Rs. {round(10, 2)}")
            fig.update_layout(legend_title='Profit value', legend_y=0.9, paper_bgcolor='#80aaff', width=width,
                              height=height)
            fig.update_traces(textinfo='percent+label', textposition='inside',
                              textfont=dict(size=14, color="white", family="Arial Black"))

            # fig.show()
            st.plotly_chart(fig, use_container_width=True, theme=None)


            # live_market = pd.DataFrame()
            # DATE = DATE_list["Date"]
            #
            #
            #
            # # index = yfinance_download_transpose.columns.get_loc(  DATE['DATE'][5])
            # live_market["DATE"] = DATE
            # live_market = pd.DataFrame(live_market["DATE"])
            #
            # print(yfinance_download_transpose.iloc[:, 0])
            # live_market["opne"] = yfinance_download1.iloc[:, 0]


            # live_market["Close"] = yfinance_download_transpose.iloc[:, index]


            # # live_market["high"] = yfinance_download_high_transpose.iloc[:, index]
            # live_market["PARSENT"] = (yfinance_download_transpose.iloc[:, index] - yfinance_download_transpose.
            #                           iloc[:, 0]) / yfinance_download_transpose.iloc[:, 0] * 100
            # print_sheets(df=live_market, sheets_name="NSE", range="A1")

            # print()
            #
            #
            #
            #
            # df = pd.DataFrame()



            # # Calculate the percentage change for each stock individually
            # percentage_change = data.pct_change().mean(axis=0) * 100
            #
            # # Calculate the current values
            # current_values = data.iloc[-1]
            #
            # # Create a DataFrame for plotly express
            # df = pd.DataFrame({'Symbols': symbols, 'Values': current_values, 'Change Percentage': percentage_change})
            #
            # # Select the top 20 values based on 'Values'
            # df_top20 = df.nlargest(15, 'Values').round(2)
            # # Round numbers to two decimal places in the text information
            # df_top20['Values'] = df_top20['Values'].round(2)
            # df_top20['Change Percentage'] = df_top20['Change Percentage'].round(2)
            #
            # # Plotting
            # fig = px.pie(df_top20, values='Values', names='Symbols',color='Symbols',
            #              hover_data=['Symbols', 'Change Percentage'],
            #              labels={'Symbols': 'Stock Symbol', 'Values': 'Value',
            #                      'Change Percentage': 'Change Percentage'},
            #              title="Top 20 Stock Portfolio Overview")
            #
            # # Add labels and values to the hover text
            # fig.update_traces(hoverinfo='label+percent+value', textinfo='label+percent+value')
            #
            # # Display the figure
            # fig.show()



run()



# streamlit run caper_14_1_2024_1.py


#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,SUZLON,BUY,MARKET,DELIVERY,111,0,0,0,0,0,0,DAY,FALSE,0,-1,"}
#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,LLOYD ,BUY,MARKET,DELIVERY ,45,0,0,0,0,0,0,DAY,FALSE,0,-1,"}