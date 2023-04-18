import yfinance as yf
# from fbprophet import Prophet
from prophet import Prophet
import plotly.graph_objs as go
# import schedule
# import smtplib
# from email.mime.text import MIMEText

# Define the list of life science companies
life_science_companies = ['JNJ', 'PFE', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BIIB', 'REGN', 'VRTX', 'ILMN']

# Define the email parameters
sender_email = 'sender_email_address'
receiver_email = 'shiyunn.dream@gmail.com'
password = 'sender_email_password'

# Define the function to retrieve and forecast the stock prices

def retrieve_and_forecast():
    # Retrieve the historical stock prices data for the past year
    data = yf.download(life_science_companies, start='2022-04-18', end='2023-04-17')
    
    # Prepare the data for Prophet
    prophet_data = data.reset_index()[['Date', 'Adj Close']]
    prophet_data.columns = ['ds', 'y']
    prophet_data['company'] = 'JNJ'
    
    # Create a Prophet model for each company and fit the data
    models = {}
    for company in life_science_companies:
        company_data = prophet_data[prophet_data['company'] == company]
        model = Prophet()
        model.fit(company_data)
        models[company] = model
    
    # Make a forecast for each company
    fig = go.Figure()
    for company in life_science_companies:
        future = models[company].make_future_dataframe(periods=365)
        forecast = models[company].predict(future)
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name=company))
    fig.update_layout(title='Life Science Companies Forecasted Prices', xaxis_title='Date', yaxis_title='Forecasted Price')
    fig.show()
    print(fig)
    
    # Send an email with the summary of the results
    # message = 'The forecasted stock prices for all life science companies are attached.'
    # msg = MIMEText(message)
    # msg['Subject'] = 'Life Science Companies Forecasted Prices'
    # msg['From'] = sender_email
    # msg['To'] = receiver_email
    
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(sender_email, password)
    #     smtp.sendmail(sender_email, receiver_email, msg.as_string())
    #     smtp.quit()

# # Schedule the script to run every day at a specified time
# schedule.every().day.at('12:00').do(retrieve_and_forecast)
