# customer_dashboard.py

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("pizza_sales.csv")

# Clean datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')


# ----- PAGE TITLE -----
st.title("🍕 Customer Behavior Dashboard - Pizza Sales")

# ---- AVERAGE ORDER VALUE ----
st.header("🚚 Average Order Value (AOV)")
order_totals = df.groupby('order_id')['total_price'].sum()
aov = order_totals.mean()
st.metric(label="Average Order Value", value=f"${aov:.2f}")

# ---- TOP ORDERS BY QUANTITY ----
st.header("📦 Top 10 Orders with Highest Quantity")
order_quantities = df.groupby('order_id')['quantity'].sum().sort_values(ascending=False)
top_orders = order_quantities.head(10)
st.dataframe(top_orders.reset_index().rename(columns={'quantity': 'Total Quantity'}))

# ---- REPEATED PIZZAS ----
st.header("🔄 Most Frequently Ordered Pizzas")

# Count number of unique orders per pizza
pizza_repeats = df.groupby('pizza_name')['order_id'].nunique().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=pizza_repeats.head(10).values,
            y=pizza_repeats.head(10).index,
            palette='rocket', ax=ax)
ax.set_title("Top 10 Most Repeated Pizzas")
ax.set_xlabel("Number of Unique Orders")
ax.set_ylabel("Pizza Name")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("👨‍💻 Dashboard by Muhammad Usama")
