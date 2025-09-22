import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 1. Load the dataset
# -----------------------------
df = pd.read_csv("trips_data-0.csv")  # <-- change file name if needed

# Convert request_time to datetime and extract hour
df['request_time'] = pd.to_datetime(df['request_time'])
df['hour'] = df['request_time'].dt.hour

# -----------------------------
# 2. Group and summarize
# -----------------------------
# Group by hour and status
hourly_counts = df.groupby(['hour', 'status']).size().unstack(fill_value=0)

# Total cancellations
cancel_cols = ['driver_canceled', 'rider_canceled', 'failed']
hourly_counts['canceled_total'] = hourly_counts[cancel_cols].sum(axis=1)

# Total rides
hourly_counts['total'] = hourly_counts['completed'] + hourly_counts['canceled_total']

# Cancellation rate
hourly_counts['cancel_rate'] = hourly_counts['canceled_total'] / hourly_counts['total']

# -----------------------------
# 3. Build Streamlit dashboard
# -----------------------------
st.title("🚖 Uber Ride Cancellations – Time Series Dashboard")

st.subheader("📊 Cancellation Data by Hour")
st.dataframe(hourly_counts)

# Bar chart: cancellations per hour
st.subheader("📉 Number of Cancellations by Hour")
fig_bar = px.bar(
    hourly_counts.reset_index(),
    x="hour",
    y="canceled_total",
    labels={"hour": "Hour of Day", "canceled_total": "Number of Cancellations"},
    hover_data=["total", "cancel_rate"],
    color="canceled_total",
    color_continuous_scale="reds"
)
st.plotly_chart(fig_bar)

# Line chart: cancellation rate per hour
st.subheader("📈 Cancellation Rate by Hour")
fig_line = px.line(
    hourly_counts.reset_index(),
    x="hour",
    y="cancel_rate",
    markers=True,
    labels={"hour": "Hour of Day", "cancel_rate": "Cancellation Rate"},
    hover_data=["canceled_total", "total"]
)
st.plotly_chart(fig_line)
