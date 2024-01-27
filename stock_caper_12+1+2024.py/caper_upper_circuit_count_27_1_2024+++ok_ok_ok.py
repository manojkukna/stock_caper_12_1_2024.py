


import os
#
# try:
#     import xlwings
# except ImportError:
#     os.system('python -m pip install --upgrade pip')
#
#
# try:
#     import openpyxl
# except ImportError:
#     os.system('python -m pip install openpyxl')

#
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


# try:
#     import pyotp
# except ImportError:
#     os.system('python -m pip install pyotp')
#
#
# try:
#     import streamlit
# except ImportError:
#     os.system('python -m pip install streamlit')
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


# import streamlit as st
# from datetime import date

# import yfinance as yf
#
# from prophet.plot import plot_plotly
# from plotly import graph_objects as go
#
# from prophet import Prophet
# import pandas as pd
import yfinance as yf
# import plotly.express as px

# streamlit run tt.py
import xlwings
import streamlit as st  #  pip install streamlit
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards
pd.set_option("display.max_rows", None)
pd.set_option("display.width",None)
pd.set_option("display.max_columns",None)

st.title('LIT FINANCE DASHBOARD')


def tickers_add_BO_NS(tickers, EXCHANGE):
    count = 0
    # print("symbol", tickers)
    for tickers_list1 in tickers:
        tickers[count] = str(f"{tickers_list1}.{EXCHANGE}")
        count = count + 1
    # print(tickers)
    return tickers


def stock_parsent(df):
     rel = df.pct_change()
     cumret = ((1+rel).cumprod() - 1) * 100
     cumret = cumret.fillna(0)
     return  cumret

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


def line_chart(data, title):
    st.line_chart(data)
    st.title(title)
    # print("line_chart 82",time_())

def convert_df(df, file_name):
    csv1 = df.to_csv().encode("utf-8")
    st.download_button(
        label="Download data as CSV",
        data=csv1,
        file_name=file_name,
        mime="text/csv", key=f"{csv1}")
    return





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



def yfinance_download_opne(tickers_list, start_date, end_date,interval):
    yfinance_download = yf.download(tickers_list, start_date, end_date, interval=interval)['Open']
    yfinance_download = yfinance_download.fillna(method='ffill', axis=0)
    yfinance_download = yfinance_download.fillna(method='bfill')
    # print(yfinance_download)
    yfinance_download.index.name = 'Date'
    yfinance_download['Date'] = pd.to_datetime(yfinance_download.index)
    yfinance_download.set_index('Date', inplace=True)
    yfinance_download.index = yfinance_download.index.strftime('%d-%m-%Y- %H:%M:%S')
    return yfinance_download


def yfinance_download_Close(tickers_list, start_date, end_date,interval):
    yfinance_download = yf.download(tickers_list, start_date, end_date, interval=interval)['Adj Close']
    print(yfinance_download)
    yfinance_download.index = yfinance_download.index.strftime("%d-%m-%Y- %H:%M:%S")





    yfinance_download = yfinance_download.fillna(method='ffill', axis=0)
    yfinance_download = yfinance_download.fillna(method='bfill')
    # print(yfinance_download)
    # breakpoint()


    return yfinance_download


def lisr_sort(df):
    lisr_sort = []
    count = 0
    count2 = len(df) - 1
    while (count < len(df)):
        count = count + 1
        count2 = count2 - 1
        lisr_sort.append(df[count2])
    return lisr_sort


def upper_circuit_count_df(df_opne,df_Close):
        df_opne = df_opne.replace([np.inf, -np.inf, np.nan], -1)
        df_Close = df_Close.replace([np.inf, -np.inf, np.nan], -1)
        upper_circuit_count = np.where(df_opne == df_Close, 1, 0)
        upper_circuit_count1 = pd.DataFrame(upper_circuit_count, columns=df_opne.columns, index=df_opne.index)
        upper_circuit_count1.index.name = 'symbol'
        upper_circuit_count = upper_circuit_count1.cumsum().transpose()
        print_sheets(df=upper_circuit_count.transpose(), sheets_name="upper_circuit_count", range="A1")
        return upper_circuit_count

def live_market_df( DATE_start, DATE_END,df_opne,df_Close):
    yfinance_download_transpose = df_Close.transpose()
    live_market = {}
    DATE_start = DATE_start
    index = yfinance_download_transpose.columns.get_loc(DATE_END)
    index_start = yfinance_download_transpose.columns.get_loc(DATE_start)

    live_market["DATE_start"] = DATE_start
    live_market["opne"] = yfinance_download_transpose.iloc[:,  index_start]
    live_market["DATE_END"] = DATE_END
    live_market["Close"] = yfinance_download_transpose.iloc[:, index]
    live_market["PARSENT"] = (yfinance_download_transpose.iloc[:,index] - yfinance_download_transpose.
                              iloc[:,index_start]) / yfinance_download_transpose.iloc[:, index_start] * 100
    live_market["CHANGE"] = yfinance_download_transpose.iloc[:, index] - yfinance_download_transpose.iloc[:, index_start]
    live_market["Rank_PARSENT"] = live_market["PARSENT"].rank(ascending=0)
    live_market_DataFrame = pd.DataFrame(live_market).round(2)
    upper_circuit_count = upper_circuit_count_df(df_opne=df_opne, df_Close=df_Close)
    live_market_DataFrame["upper_circuit"] = upper_circuit_count.iloc[:, index]
    live_market_DataFrame.sort_values("Rank_PARSENT", axis=0, ascending=True, inplace=True)
    live_market_DataFrame.index.name = 'symbol'
    return  live_market_DataFrame






import streamlit as st
from datetime import datetime



sheets_list = ["NSE", "holdings", "orders", "Adj Close", "Volume",
               "HIGH", "upper_circuit_count"]
exl_sheets_list(exl_sheets_list=sheets_list)

def run():


        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Sector', 'all MARRKET'], #'Add Your Capital', 'Holding', 'Intraday', 'Options', 'Charges',
                         # 'Charges Debits and Credits', 'Dividends', 'Settings', 'about'],
                #           https: // icons.getbootstrap.com /  # icons     'person-circle'

                icons=['house-fill', 'journal-arrow-up'],#, 'journal-arrow-up', 'trophy-fill', 'apple', 'play-btn-fill',
                       #'caret-right-square-fill', 'caret-right-square-fill', 'caret-right-square-fill', 'gear',
                       #'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "30px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"}, })


        if app == 'all MARRKET':
            NSE_all = pd.read_csv("NSE.csv")

            selected_stock_Sector = st.selectbox('selected dataset for  INDEX', NSE_all['Sector'].unique(),
                                                         key='Sector')
            selected_stock_EXCHANGE = st.selectbox('selected dataset for  EXCHANGE', ['BSE', 'NSE'],
                                                           key='EXCHANGE')
            NSE_df = NSE_all.loc[
                (NSE_all["Sector"] == selected_stock_Sector) & (NSE_all["Exchange"] == selected_stock_EXCHANGE)]
            EXCHANGE = {"BSE": 'BO', "NSE": 'NS'}
            data_tickers = tickers_add_BO_NS(tickers=NSE_df['Ticker'].tolist(),
                                             EXCHANGE=EXCHANGE[selected_stock_EXCHANGE])
            #
            # if selected_stock_Sector == "Sector":
            #     NSE_all = pd.read_csv("NSE.csv")
            #     NSE_df2 = NSE_all.loc[(NSE_all["Exchange"] == 'NSE')]
            #     BSE_df2 = NSE_all.loc[(NSE_all["Exchange"] == 'BSE')]
            #
            #     remove_duplicates_NSC_ALL = [number for number in list(NSE_df2["Ticker"].values) if
            #                                  number not in list(BSE_df2["Ticker"].values)]
            #     remove_duplicates_BSE_ALL = [number for number in list(BSE_df2["Ticker"].values) if
            #                                  number not in remove_duplicates_NSC_ALL]
            #     data_tickers = tickers_add_BO_NS(tickers=remove_duplicates_NSC_ALL, EXCHANGE="NS") + tickers_add_BO_NS(
            #         tickers=remove_duplicates_BSE_ALL, EXCHANGE="BO")



            start_user_Date = st.date_input('Start Date', value=pd.to_datetime('2023-12-01'), key='start')
            default_time = datetime.strptime("00:00:00", "%H:%M:%S").time()
            start_user_time = st.time_input("start_user a time", value=default_time)

            start_user_Date_datetime = datetime.combine( start_user_Date,start_user_time)
            start_user_Date_datetime_formatted = start_user_Date_datetime.strftime("%d-%m-%Y- %H:%M:%S")
            st.write("start_user_Date You selected:", start_user_Date_datetime_formatted)




            selected_interval = st.selectbox('selected dataset for selected_interval', ['1d', '15m', '2m', '5m', '10m', '15m', '30m'], key='interval')

            yfinance_download_Close1 = yfinance_download_Close(tickers_list=data_tickers, start_date=start_user_Date, end_date=None , interval=selected_interval)
            yfinance_download_opne1 = yfinance_download_opne(tickers_list=data_tickers, start_date= start_user_Date, end_date=None, interval=selected_interval)
            BSE_Close_to_csv = yfinance_download_Close1.to_csv("BSE_Close.csv", mode='w', index=True, header=True)
            BSE_opne_to_csv = yfinance_download_opne1.to_csv("BSE_opne.csv", mode='w', index=True, header=True)

            print(BSE_opne_to_csv)


            # breakpoint()



        if app == "Sector":



            BSE_Close_csv_read = pd.DataFrame(pd.read_csv("BSE_Close.csv", on_bad_lines='skip'))
            BSE_Close = BSE_Close_csv_read.loc[:, ~ BSE_Close_csv_read.columns.str.contains('^Unnamed')]
            #
            # print(BSE_Close.head(10))

            BSE_Close  = pd.read_csv("BSE_Close.csv", index_col=None)
            BSE_Close['Date'] = pd.to_datetime(BSE_Close['Date'], format="%d-%m-%Y- %H:%M:%S")
            BSE_Close=   BSE_Close.set_index('Date')

            # breakpoint()
            BSE_opne_csv_read = pd.DataFrame(pd.read_csv("BSE_opne.csv", on_bad_lines='skip'))
            BSE_opne =  BSE_opne_csv_read.loc[:, ~ BSE_opne_csv_read.columns.str.contains('^Unnamed')]
            BSE_opne['Date'] = pd.to_datetime(BSE_opne['Date'], format="%d-%m-%Y- %H:%M:%S")
            BSE_opne = BSE_opne.set_index('Date')
            # print(BSE_Close.head(10))

            print_sheets(df=BSE_opne, sheets_name="opne", range="A1")

            print_sheets(df=BSE_Close, sheets_name="Adj Close", range="A1")

            # start_user_Date_sidebar = st.sidebar.date_input('Start Date', value=pd.to_datetime('2023-12-01'), key='Sector_start')
            # default_time = datetime.strptime("00:00:00", "%H:%M:%S").time()
            # start_user_time = st.time_input("start_user a time", value=default_time,key='start_user_time')

            top_20 = st.number_input(" top_21", value=15, key='top_21')
            Rank_circuit = st.number_input("Rank_circuit", value=15, key='Rank_circuit')

            # start_user_Date_datetime = datetime.combine(start_user_Date_sidebar, start_user_time)
            # start_user_Date_datetime_formatted = start_user_Date_datetime.strftime("%d-%m-%Y- %H:%M:%S")
            # st.write("You selected:", start_user_Date_datetime_formatted)

            last_date_formatted = lisr_sort(df=BSE_Close.index.tolist())
            print( last_date_formatted )
            #

            # # Set a default value for the selectbox
            # default_value = Timestamp('2024-01-24 00:00:00')

            # # Create a selectbox with a default value
            # selected_timestamp = st.selectbox('Select a Timestamp',  last_date_formatted, index=0)

            start_user_Date_datetime = st.sidebar.selectbox("start_user Select a Date",BSE_Close.index.tolist())

            end_user_Date_datetime = st.sidebar.selectbox("end_user Select a Date",last_date_formatted)






            live_market_data = live_market_df( DATE_start=start_user_Date_datetime , DATE_END= end_user_Date_datetime,df_opne= BSE_opne,df_Close=BSE_Close)

            live_market_data = pd.DataFrame(live_market_data)

            #
            # print(live_market_data.index)
            # print(live_market_data.columns)






            live_market_data = live_market_data.loc[live_market_data['upper_circuit'] < ((len( BSE_Close) / 100) * Rank_circuit)]

            live_market_data1 = live_market_data.loc[live_market_data['PARSENT'] >= 0]

            live_market_data = pd.DataFrame(live_market_data1).head(top_20)
            print_sheets(df=live_market_data, sheets_name="NSE", range="A1")





            fig = px.pie(live_market_data.round(2), values='PARSENT', names=live_market_data.index,# color=live_market_data.index,
                         # color_discrete_map=custom_colors,
                         title=f"ALL DATA piy chaty = Rs. {round(10, 2)}")
            fig.update_layout(legend_title='Profit value', legend_y=0.9, paper_bgcolor='#80aaff', width=width,
                              height=height)
            fig.update_traces(textinfo='label+percent+value', textposition='inside',
                              textfont=dict(size=14, color="white", family="Arial Black"))
            st.plotly_chart(fig, use_container_width=True, theme=None)
            st.dataframe(live_market_data1.round(2), use_container_width=False, width=1200, height=300)
            convert_df(df=live_market_data1, file_name="manoj kukana ")





run()



# streamlit run caper_upper_circuit_count_27_1_2024+++.py


#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,SUZLON,BUY,MARKET,DELIVERY,111,0,0,0,0,0,0,DAY,FALSE,0,-1,"}
#    {"Apikey":"IP8LS9IO4PAI8VF ","command": "PLACE_ORDER,LG5706,0,REGULAR,NSE,LLOYD ,BUY,MARKET,DELIVERY ,45,0,0,0,0,0,0,DAY,FALSE,0,-1,"}