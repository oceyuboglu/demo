import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
@st.cache
def load_data():
    # Sample data
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=100),
        'Sales': [100, 120, 90, 110, 105, 115, 130, 140, 120, 125, 
                  130, 135, 145, 150, 160, 155, 165, 170, 180, 190] * 5,
        'Profit': [20, 25, 18, 22, 21, 23, 26, 28, 24, 25, 
                   26, 27, 29, 30, 32, 31, 33, 34, 36, 38] * 5
    }
    df = pd.DataFrame(data)
    return df

def main():
    st.title('Business Intelligence Dashboard')

    df = load_data()

    # Set up sidebar
    st.sidebar.title('Filters')
    date_range = st.sidebar.date_input('Select Date Range', [df['Date'].min(), df['Date'].max()])

    # Filter data based on date range
    filtered_df = df[(df['Date'] >= date_range[0]) & (df['Date'] <= date_range[1])]

    # Sales and Profit visualization
    st.header('Sales and Profit Analysis')
    st.subheader('Sales and Profit Over Time')

    # Line chart for Sales and Profit over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_df, x='Date', y='Sales', label='Sales')
    sns.lineplot(data=filtered_df, x='Date', y='Profit', label='Profit')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Sales and Profit Over Time')
    plt.legend()
    st.pyplot()

    # Monthly Sales and Profit Summary
    st.subheader('Monthly Sales and Profit Summary')

    # Group by month
    monthly_summary = filtered_df.resample('M', on='Date').sum()

    # Bar chart for monthly sales and profit
    plt.figure(figsize=(10, 6))
    monthly_summary.plot(kind='bar', stacked=True)
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Monthly Sales and Profit Summary')
    plt.xticks(rotation=45)
    st.pyplot()

if __name__ == "__main__":
    main()
