import streamlit as st

def render_efficiency_panels_module(df):
    st.markdown("### ⚡ Operational Segment Efficiency")
    
    latest = df.iloc[-1]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Current Transfer Efficiency Ratio", 
            value=f"{latest['transfer_efficiency_ratio']*100:.1f}%",
            delta=f"{(latest['transfer_efficiency_ratio'] - df['transfer_efficiency_ratio'].mean())*100:.1f}% vs Avg"
        )
        st.caption("Target: > 30% daily operational clearance speed from CBP custody to HHS shelters.")
        
    with col2:
        st.metric(
            label="Current Discharge Effectiveness Index", 
            value=f"{latest['discharge_effectiveness_index']*100:.2f}%",
            delta=f"{(latest['discharge_effectiveness_index'] - df['discharge_effectiveness_index'].mean())*100:.2f}% vs Avg"
        )
        st.caption("Target: Consistent upward baseline indicating rapid verification and family reunification.")