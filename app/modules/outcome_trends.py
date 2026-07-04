import streamlit as st

def render_outcome_trends_module(df):
    st.markdown("### 🚨 Pipeline Stability & Throughput Trends")
    
    recent_throughput = df['pipeline_throughput_rate'].tail(14).mean()
    
    if recent_throughput < 1.0:
        st.error(f"⚠️ **System Alert:** Recent 14-day pipeline throughput is **{recent_throughput:.2f}**. The system is currently absorbing more children than it is releasing. Backlog risk is elevated.")
    else:
        st.success(f"✅ **System Stable:** Recent 14-day pipeline throughput is **{recent_throughput:.2f}**. Discharges are successfully outstripping incoming arrivals.")