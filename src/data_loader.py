# src/data_loader.py
import pandas as pd
import numpy as np
import os

def load_clean_uac_data(uploaded_file=None):
    """
    Scans the project directory to locate the UAC dataset dynamically,
    bypassing static folder path constraints. If a file is uploaded
    via Streamlit, it switches seamlessly to processing that uploaded buffer.
    """
    target_substring = "HHS_Unaccompanied_Alien_Children_Program"
    
    # 1. Select the Data Source: Streamlit Uploader Buffer vs. Local Directory Walk
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            print("Successfully loaded user-uploaded dataset from Streamlit.")
        except Exception as e:
            raise ValueError(f"CRITICAL: Failed to parse uploaded CSV file. Error: {e}")
    else:
        # Track current directory tree roots
        current_file_path = os.path.abspath(__file__)
        src_folder = os.path.dirname(current_file_path)
        project_root = os.path.dirname(src_folder)
        
        filepath = None
        
        # 2. Walk through all folders to find where the file is hiding
        for root, dirs, files in os.walk(project_root):
            for f in files:
                if target_substring in f:
                    filepath = os.path.join(root, f)
                    break
            if filepath:
                break
                
        if not filepath:
            raise FileNotFoundError(
                f"CRITICAL: Could not find any file matching '{target_substring}' anywhere inside '{project_root}'."
                "\nPlease verify that you have downloaded the file into this project folder."
            )

        print(f"Successfully auto-detected data file at: {filepath}")

        # Load data
        df = pd.read_csv(filepath)
    
    # Drop rows that are completely empty or missing the critical Date field
    df = df.dropna(subset=['Date'])
    
    # Map raw columns to standardized, clean script variables
    column_mapping = {
        'Date': 'date',
        'Children apprehended and placed in CBP custody*': 'cbp_intake',
        'Children in CBP custody': 'cbp_stock',
        'Children transferred out of CBP custody': 'cbp_transfer_out',
        'Children in HHS Care': 'hhs_stock',
        'Children discharged from HHS Care': 'hhs_discharge_out'
    }
    df = df.rename(columns=column_mapping)
    df.columns = df.columns.str.strip()
    
    # Clean numeric fields, removing commas and converting text values to numeric
    numeric_cols = [
        'hhs_stock',
        'cbp_intake',
        'cbp_stock',
        'cbp_transfer_out',
        'hhs_discharge_out'
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Convert date format and sort chronologically
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    test_df = load_clean_uac_data()
    print(test_df.head(3))