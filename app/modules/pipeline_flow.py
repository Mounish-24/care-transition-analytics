import streamlit as st
from src.visualizations import plot_pipeline_volume_trends

def render_pipeline_flow_module(df):
    st.markdown("### 📈 Pipeline Flow & Capacity Distribution")
    st.pyplot(plot_pipeline_volume_trends(df))
    
    with st.expander("🔍 Strategic Insights (Operational Lens)"):
        st.markdown("""
        * **Inventory Divergence:** When CBP custody drops while HHS care climbs, it signals that the intake bottleneck is cleared, but the discharge/placement phase is under heavy load.
        * **Logistical Friction:** Sudden spikes in CBP custody indicate immediate transportation or inter-agency handover delays.
        """)