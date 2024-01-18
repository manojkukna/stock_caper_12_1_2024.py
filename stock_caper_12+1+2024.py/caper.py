


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

stock_INDEX = ["NIFTY 20","NIFTY 50","NIFTY NEXT 50","NIFTY 200",
              "NIFTY MIDCAP 50","NIFTY MIDCAP 100","NIFTY MIDSMALLCAP 400","NIFTY MIDSMALLCAP 400","NIFTY TOTAL MARKET"]


# selected_stock_INDEX = st.selectbox('selected dataset for  INDEX',stock_INDEX)
# EXCHANGE ={"BSE":'BO',"NSE":'NS' }
# tickers = list(data1[selected_stock_INDEX].values)
# selected_stock_EXCHANGE = st.selectbox('selected dataset for  EXCHANGE',['BSE','NSE'])
# data_tickers = tickers_add_BO_NS(tickers=tickers, EXCHANGE=EXCHANGE[selected_stock_EXCHANGE])
#
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





def run():

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

            # stocks = ('RELI', 'TCS.BO', 'WIT', 'INFY')
            # dropdown = st.sidebar.multiselect('pick your assets', stocks)

            start = st.sidebar.date_input('Start Date', value=pd.to_datetime('2020-01-01'))
            end = st.sidebar.date_input('End Date', value=pd.to_datetime('today'))
            import matplotlib.pyplot as plt

            # Fetch historical data for the stocks
            data = yf.download(data_tickers, start=start, end=end)['Adj Close']



            portfolio_percentages = data.iloc[-1] / data.iloc[-1].sum()

            profitable_stocks = portfolio_percentages.index[portfolio_percentages >= 0]





            # Create a new Series with only profitable stocks
            profit_pie = portfolio_percentages[profitable_stocks]

            print(profit_pie)
            # Create a pie chart for profitable stocks
            plt.figure(figsize=(8, 8))
            plt.pie(profit_pie, labels=profit_pie.index, autopct='%1.1f%%', startangle=140)
            plt.title('Profitable Stock Portfolio Composition')
            plt.show()




            # Create a pie chart
            # plt.figure(figsize=(8, 8))
            # plt.pie(portfolio_percentages, labels=data_tickers, autopct='%1.1f%%', startangle=140)
            # plt.title('Stock Portfolio Composition')
            # plt.show()
            #
            # percentage = ((df - df.shift(1)) / df.shift(1)) * 100
               # print(pd.DataFrame(percentage).sum())

            # percentage_cumsum = percentage.cumsum(axis='rows')  # df.cumsum(axis='columns')
            #    # percentage_cumsum = pd.DataFrame(percentage)
            #
            # print(percentage_cumsum.tail(1))
            #
            #
            #
            # piny_df =pd.DataFrame(percentage_cumsum.head(10).sum())
            #    # print(percentage_cumsum.head(10).sum())
            #    # print(piny_df.)
            #    # print(piny_df.columns[0])
            #
            #    chang = pd.DataFrame()
            #    chang["symbol"] = percentage_cumsum.columns
            #    chang["chang"] = percentage_cumsum.iloc[len(percentage_cumsum)-1, 1]
            #
            #
            #    print(chang)
            #
            #
            #    st.title('STOCK percentage')
            #    st.write(percentage_cumsum)
            #    # percentage_cumsum = percentage_cumsum1.transpose()
            #    st.title(selected_stock_INDEX)
            #    st.line_chart(percentage_cumsum)




run()



# streamlit run caper.py


#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,SUZLON,BUY,MARKET,DELIVERY,111,0,0,0,0,0,0,DAY,FALSE,0,-1,"}
#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,LLOYD ,BUY,MARKET,DELIVERY ,45,0,0,0,0,0,0,DAY,FALSE,0,-1,"}