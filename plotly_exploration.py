import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Create a sample stocks DataFrame (You can replace this with your actual data)
dates = pd.date_range(start="2024-01-01", periods=10, freq="D")
stocks = ["AAPL", "GOOGL", "AMZN", "MSFT"]
prices = np.random.normal(loc=150, scale=30, size=(10, 4))  # Random stock prices

# Create a DataFrame with dates and stock prices
stocks_long = pd.DataFrame(prices, columns=stocks)
stocks_long["date"] = dates
stocks_long = stocks_long.melt(id_vars=["date"], var_name="stock", value_name="price")

# Generate very uneven trading volume using log-normal distribution
mean_log = 6  # Adjust for lower mean
sigma_log = 1.5  # Increase sigma for a wider spread, highly skewed

stocks_long["Volume"] = np.random.lognormal(mean=mean_log, sigma=sigma_log, size=stocks_long.shape[0])

# Scale to realistic stock trading volumes
stocks_long["Volume"] *= 20  # Increase scale for more visibility

# Streamlit Title
st.title("Stock Prices and Trading Volume (Bubble Chart)")

# Plot the Bubble Chart with Animation
fig = px.scatter(stocks_long, 
                 x="date", 
                 y="price", 
                 size="Volume",  # Bubble size represents trading volume
                 color="stock",  # Different colors for different stocks
                 title="Stock Prices and Highly Uneven Trading Volume Over Time",
                 hover_data=["stock", "Volume"],
                 animation_frame="date",  # Animate by date
                 animation_group="stock",  # Keep the same stock together during animation
                 range_y=[stocks_long["price"].min() - 10, stocks_long["price"].max() + 10],  # Optional: Adjust Y-axis range for clarity
                 range_x=[stocks_long["date"].min(), stocks_long["date"].max()]  # Optional: Adjust X-axis range for clarity
)

# Show the plot in Streamlit
st.plotly_chart(fig)



#Use st.slider() to let users select the range of dates.
#Use st.selectbox() to allow users to choose specific stocks.
