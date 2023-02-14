import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

# Download historical stock prices from Yahoo Finance
apple_stock = yf.download("ABBV", start="2010-01-01", end="2023-02-14")

# Visualize the data
apple_stock["Adj Close"].plot()
plt.title("ABBV Stock Prices")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.show()

# Prepare the data for Prophet forecasting
df = apple_stock.reset_index()[["Date", "Adj Close"]]
df = df.rename(columns={"Date": "ds", "Adj Close": "y"})

# Train the Prophet model
model = Prophet()
model.fit(df)

# Prompt the user to enter a future date for prediction
while True:
    try:
        user_date = input("Enter a future date (in YYYY-MM-DD format): ")
        future_date = pd.to_datetime(user_date)
        break
    except ValueError:
        print("Invalid date format. Please try again.")

# Make a prediction for the future date entered by the user
future = pd.DataFrame({"ds": [future_date]})
forecast = model.predict(future)

# Display the prediction to the user
print("Predicted ABBV stock price on", user_date, "is $", round(forecast['yhat'][0], 2))

# Make a prediction for a range of future dates
future_range = pd.date_range(start=max(df['ds']), end=future_date, freq='D')
future = pd.DataFrame({"ds": future_range})
forecast = model.predict(future)

# Visualize the forecast
model.plot(forecast, xlabel="Date", ylabel="Adjusted Close Price")
plt.title("Apple Stock Price Forecast")
plt.axvline(x=future_date, color='r', linestyle='--')
plt.show()
