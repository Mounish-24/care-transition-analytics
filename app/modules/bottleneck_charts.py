import streamlit as st
from src.visualizations import plot_day_of_week_bottlenecks

def render_bottleneck_charts_module(df):
    st.markdown("### ⏳ Systemic Delay & Blockage Point Isolation")
    st.pyplot(plot_day_of_week_bottlenecks(df))
    
    st.info(
        "💡 **Judges' Tip:** Notice the weekend drop-offs. Operational efficiency typically nose-dives "
        "on Saturdays and Sundays due to reduced court, administrative, and vetting personnel presence."
    )