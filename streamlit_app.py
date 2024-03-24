import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Function to fetch data from API with basic authentication
def fetch_data_from_api(url, username, password):
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

# Streamlit app
def main():
    st.title('BI Dashboard')

    # Sidebar - Authentication
    st.sidebar.title('Authentication')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')

    # Fetch data from API
    if st.sidebar.button('Fetch Data'):
        if not username or not password:
            st.sidebar.error('Please provide username and password.')
        else:
            url = 'https://api.evocon.com/api/reports/oee_json?stationId=1&stationId=2&startTime=2024-01-01&endTime=2025-06-10'  # Replace with your API URL
            data = fetch_data_from_api(url, username, password)
            if data is not None:
                st.success('Data fetched successfully.')
                st.write(data)

                # Sales and Profit visualization
                st.header('Sales and Profit Analysis')

                # Line chart for Sales and Profit over time
                plt.figure(figsize=(10, 6))
                sns.lineplot(data=data, x='Date', y='Sales', label='Sales')
                sns.lineplot(data=data, x='Date', y='Profit', label='Profit')
                plt.xlabel('Date')
                plt.ylabel('Amount')
                plt.title('Sales and Profit Over Time')
                plt.legend()
                st.pyplot()

                # Monthly Sales and Profit Summary
                st.header('Monthly Sales and Profit Summary')

                # Group by month
                monthly_summary = data.resample('M', on='Date').sum()

                # Bar chart for monthly sales and profit
                plt.figure(figsize=(10, 6))
                monthly_summary.plot(kind='bar', stacked=True)
                plt.xlabel('Month')
                plt.ylabel('Amount')
                plt.title('Monthly Sales and Profit Summary')
                plt.xticks(rotation=45)
                st.pyplot()

# Run the Streamlit app
if __name__ == "__main__":
    main()
