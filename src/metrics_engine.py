# src/metrics_engine.py
import pandas as pd
import numpy as np
from src.data_loader import load_clean_uac_data

def calculate_pipeline_metrics(df):
    """
    Applies operational pipeline equations to derive transition speed,
    effectiveness indexes, and system backlog velocity.
    """
    metrics_df = df.copy()
    
    # Avoid zero division bugs by substituting 0 with NaN dynamically during math operations
    metrics_df['transfer_efficiency_ratio'] = (
        metrics_df['cbp_transfer_out'] / metrics_df['cbp_stock'].replace(0, np.nan)
    )
    
    metrics_df['discharge_effectiveness_index'] = (
        metrics_df['hhs_discharge_out'] / metrics_df['hhs_stock'].replace(0, np.nan)
    )
    
    metrics_df['pipeline_throughput_rate'] = (
        metrics_df['hhs_discharge_out'] / metrics_df['cbp_intake'].replace(0, np.nan)
    )
    
    # Net flow accumulation rates
    metrics_df['net_backlog_change'] = metrics_df['cbp_intake'] - metrics_df['hhs_discharge_out']
    
    # Temporal variables for bottleneck trend detection
    metrics_df['day_of_week'] = metrics_df['date'].dt.day_name()
    metrics_df['month_year'] = metrics_df['date'].dt.to_period('M')
    
    return metrics_df

if __name__ == "__main__":
    raw_data = load_clean_uac_data()
    processed_data = calculate_pipeline_metrics(raw_data)
    print("\n--- Processed Metric Analytics Sample ---")
    print(processed_data[['date', 'transfer_efficiency_ratio', 'discharge_effectiveness_index', 'net_backlog_change']].tail())