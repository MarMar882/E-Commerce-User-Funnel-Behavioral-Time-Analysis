import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_combined_data

# Load data
df = load_combined_data()

# Filter purchase events
df_purchase = df[df['event_type'] == 'purchase'].copy()
df_purchase['event_date'] = df_purchase['event_time'].dt.date

# Count purchases per day
daily_purchases = df_purchase.groupby('event_date').size()

# Plot
plt.figure(figsize=(14, 6))
daily_purchases.plot(kind='line', marker='o', color='steelblue')
plt.title("Daily Number of Purchases (Oct + Nov 2019)")
plt.xlabel("Date")
plt.ylabel("Number of Purchases")
plt.grid(True, linestyle='--', alpha=0.4)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
