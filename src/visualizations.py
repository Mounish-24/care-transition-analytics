# src/visualizations.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set clean, professional visual themes for government stakeholders
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 13})

def plot_pipeline_volume_trends(df):
    """
    Generates a time-series plot comparing the active stock layers 
    (CBP Custody vs HHS Care Over Time) using dual Y-axes to resolve
    severe inventory scale mismatches.
    """
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # 1. Plot CBP Custody Stock on the Primary (Left) Y-Axis
    line1, = ax1.plot(
        df['date'], 
        df['cbp_stock'], 
        label='Children in CBP Custody', 
        color='#1f77b4', 
        linewidth=2
    )
    ax1.set_xlabel('Reporting Timeline', fontweight='bold')
    ax1.set_ylabel('Active CBP Stock (Left Axis)', color='#1f77b4', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#1f77b4')
    
    # 2. Create a Secondary Y-Axis sharing the same X-axis for HHS Care Volume
    ax2 = ax1.twinx()
    line2, = ax2.plot(
        df['date'], 
        df['hhs_stock'], 
        label='Children in HHS Care', 
        color='#ff7f0e', 
        linewidth=2
    )
    ax2.set_ylabel('Active HHS Care Stock (Right Axis)', color='#ff7f0e', fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='#ff7f0e')
    
    # Remove the automatic secondary background grid lines to prevent overlapping grid clutter
    ax2.grid(False)
    
    # 3. Combine both lines cleanly into a unified legend box
    lines = [line1, line2]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right', frameon=True)
    
    ax1.set_title('UAC Custody Inventory Trends (CBP vs. HHS)', pad=12)
    plt.tight_layout()
    return fig

def plot_day_of_week_bottlenecks(df):
    """
    Aggregates efficiency ratios by weekday to highlight processing slowdowns.
    """
    # Force chronological weekday ordering
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Calculate average efficiency metrics grouped by weekday
    weekday_summary = df.groupby('day_of_week')[['transfer_efficiency_ratio', 'discharge_effectiveness_index']].mean().reindex(days_order)
    weekday_summary = weekday_summary.reset_index()
    
    # Melt dataframe for structured seaborn plotting
    melted_df = weekday_summary.melt(id_vars='day_of_week', var_name='Metric', value_name='Rate')
    melted_df['Metric'] = melted_df['Metric'].map({
        'transfer_efficiency_ratio': 'CBP → HHS Transfer Speed',
        'discharge_effectiveness_index': 'HHS Placement Release Rate'
    })

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=melted_df, x='day_of_week', y='Rate', hue='Metric', palette='muted', ax=ax)
    
    ax.set_title('Operational Processing Velocity by Day of Week')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Average Processing Efficiency Ratio')
    ax.legend(title='Pipeline Segment')
    plt.tight_layout()
    return fig

def plot_backlog_accumulation(df):
    """
    Plots a rolling sum of Net Backlog Velocity to isolate system crisis periods.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Compute 7-day rolling window to smooth out irregular weekend data reporting gaps
    df['rolling_backlog'] = df['net_backlog_change'].rolling(window=7, center=True).mean()
    
    # Plot positive accumulation as Red (System Overload) and Negative as Green (Clearing Out)
    ax.fill_between(df['date'], df['rolling_backlog'], 0, 
                    where=(df['rolling_backlog'] >= 0), color='#d62728', alpha=0.6, label='Net Backlog Accumulation (Inflow > Discharges)')
    ax.fill_between(df['date'], df['rolling_backlog'], 0, 
                    where=(df['rolling_backlog'] < 0), color='#2ca02c', alpha=0.6, label='Net System Clearance (Discharges > Inflow)')
    
    ax.axhline(0, color='black', linestyle='--', linewidth=1)
    ax.set_title('Pipeline Velocity & Backlog Volatility (7-Day Rolling Baseline)')
    ax.set_xlabel('Reporting Timeline')
    ax.set_ylabel('Net Daily Case Delta')
    ax.legend(loc='upper right', frameon=True)
    plt.tight_layout()
    return fig