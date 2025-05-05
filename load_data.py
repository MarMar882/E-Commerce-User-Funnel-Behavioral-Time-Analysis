import pandas as pd

def load_combined_data(parse_dates=True, nrows=None):
    """
    Loads and combines October and November datasets.
    
    Args:
        parse_dates (bool): Whether to parse 'event_time' as datetime.
        nrows (int or None): Limit the number of rows for quick testing.
    
    Returns:
        DataFrame: Combined DataFrame from both months.
    """
    df_oct = pd.read_csv("2019-Oct.csv", parse_dates=['event_time'] if parse_dates else None, nrows=nrows)
    df_nov = pd.read_csv("2019-Nov.csv", parse_dates=['event_time'] if parse_dates else None, nrows=nrows)
    df_all = pd.concat([df_oct, df_nov], ignore_index=True)
    return df_all
