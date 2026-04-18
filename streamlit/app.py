import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="Customer Engagement & Product Utilization Analytics for Retention Strategy Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/European_Bank.csv")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filters")
min_balance = st.sidebar.slider("Minimum Balance", 0, int(df["Balance"].max()), 50000, step=5000)
product_count = st.sidebar.slider("Minimum Product Count", 1, int(df["NumOfProducts"].max()), 2)
activity_filter = st.sidebar.selectbox("Activity Status", ["All", "Active", "Inactive"])

# Apply filters
filtered_df = df.copy()
if activity_filter == "Active":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 1]
elif activity_filter == "Inactive":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 0]
filtered_df = filtered_df[filtered_df["Balance"] >= min_balance]
filtered_df = filtered_df[filtered_df["NumOfProducts"] >= product_count]

# --- Title Space ---
st.title("📊 Customer Engagement & Product Utilization Analytics for Retention Strategy Dashboard")
st.markdown("Interactive exploration of churn KPIs, engagement insights, and product depth.")

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "KPIs", "Engagement Analysis", "Product Utilization", "Premium Risk", "Relationship Strength"
])

# --- KPI Tab ---
with tab1:
    st.subheader("Key Performance Indicators")

    def safe_mean(subset):
        return subset["Exited"].mean() * 100 if not subset.empty else 0

    active_churn = safe_mean(filtered_df[filtered_df["IsActiveMember"] == 1])
    inactive_churn = safe_mean(filtered_df[filtered_df["IsActiveMember"] == 0])
    high_balance_churn = safe_mean(filtered_df[filtered_df["Balance"] >= 100000])
    others_churn = safe_mean(filtered_df[filtered_df["Balance"] < 100000])
    card_churn = safe_mean(filtered_df[filtered_df["HasCrCard"] == 1])
    non_card_churn = safe_mean(filtered_df[filtered_df["HasCrCard"] == 0])

    # Two rows of metrics (3 per row)
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Churn Rate", f"{active_churn:.1f}%")
    col2.metric("Inactive Churn Rate", f"{inactive_churn:.1f}%")
    col3.metric("High Balance Churn", f"{high_balance_churn:.1f}%")

    col4, col5, col6 = st.columns(3)
    col4.metric("Others Churn Rate", f"{others_churn:.1f}%")
    col5.metric("Credit Card Holders Churn", f"{card_churn:.1f}%")
    col6.metric("Non-Card Holders Churn", f"{non_card_churn:.1f}%")

# --- Engagement Analysis ---
with tab2:
    st.subheader("Engagement vs Churn Overview")
    engagement_data = pd.DataFrame({
        "Status": ["Active","Inactive"],
        "ChurnRate": [active_churn, inactive_churn]
    })
    max_val = engagement_data["ChurnRate"].max()
    fig = px.bar(
        engagement_data,
        x="Status",
        y="ChurnRate",
        color="Status",
        text=engagement_data["ChurnRate"].round(1),
        labels={"ChurnRate":"Churn Rate (%)"},
        title="Churn Rate: Active vs Inactive",
        color_discrete_map={"Active":"green","Inactive":"red"}
    )
    fig.update_traces(textposition="outside", textfont_size=16)
    fig.update_layout(
        title_font_size=22, xaxis_title_font_size=18, yaxis_title_font_size=18,
        yaxis=dict(range=[0, max_val + 10])
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Product Utilization ---
with tab3:
    st.subheader("Product Depth Index")
    churn_by_products = filtered_df.groupby("NumOfProducts")["Exited"].mean().reset_index(name="ChurnRate")
    churn_by_products["NumOfProducts"] = churn_by_products["NumOfProducts"].astype(int)  # ensure whole numbers
    max_val = churn_by_products["ChurnRate"].max()
    fig = px.bar(
        churn_by_products,
        x="NumOfProducts",
        y="ChurnRate",
        color="NumOfProducts",
        text=churn_by_products["ChurnRate"].round(0),  # no decimals
        labels={"NumOfProducts":"Products Held","ChurnRate":"Churn Rate (%)"},
        title="Churn by Product Depth"
    )
    fig.update_traces(textposition="outside", textfont_size=16)
    fig.update_layout(
        title_font_size=22, xaxis_title_font_size=18, yaxis_title_font_size=18,
        xaxis=dict(dtick=1),  # step count = 1
        yaxis=dict(range=[0, max_val + 5])  # reduced buffer
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Premium Risk ---
with tab4:
    st.subheader("High-Value Disengaged Customers")
    max_val = max(high_balance_churn, others_churn)
    fig = px.bar(
        x=["High Balance","Others"],
        y=[high_balance_churn, others_churn],
        color=["High Balance","Others"],
        text=[f"{high_balance_churn:.1f}%", f"{others_churn:.1f}%"],
        labels={"x":"Segment","y":"Churn Rate (%)"},
        title="High-Balance Disengagement Rate",
        color_discrete_map={"High Balance":"orange","Others":"blue"}
    )
    fig.update_traces(textposition="outside", textfont_size=16)
    fig.update_layout(
        title_font_size=22, xaxis_title_font_size=18, yaxis_title_font_size=18,
        yaxis=dict(range=[0, max_val + 10])
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Relationship Strength ---
with tab5:
    st.subheader("Relationship Strength Index")
    filtered_df["Tier"] = filtered_df.apply(
        lambda row: 2 if row["IsActiveMember"]==1 and row["NumOfProducts"]>1
        else 0 if row["IsActiveMember"]==0 and row["NumOfProducts"]==1
        else 1, axis=1
    )
    tier_map = {0:"Weak",1:"Moderate",2:"Strong"}
    churn_by_tier = filtered_df.groupby("Tier")["Exited"].mean().reset_index(name="ChurnRate")
    churn_by_tier["TierLabel"] = churn_by_tier["Tier"].map(tier_map)
    max_val = churn_by_tier["ChurnRate"].max()

    fig = px.bar(
        churn_by_tier,
        x="TierLabel",
        y="ChurnRate",
        color="TierLabel",
        text=churn_by_tier["ChurnRate"].round(2),  # ✅ show decimals (2 places)
        labels={"TierLabel":"Relationship Tier","ChurnRate":"Churn Rate (%)"},
        title="Churn by Relationship Strength"
    )
    fig.update_traces(textposition="outside", textfont_size=16)
    fig.update_layout(
        title_font_size=22, xaxis_title_font_size=18, yaxis_title_font_size=18,
        yaxis=dict(range=[0, max_val + 5])
    )
    st.plotly_chart(fig, use_container_width=True)
