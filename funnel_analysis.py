import pandas as pd
import matplotlib.pyplot as plt
import os
from load_data import load_combined_data

# Load data
df_all = load_combined_data(nrows=200000)

# Keep only session and event_type
df = df_all[['user_session', 'event_type']].drop_duplicates()

# Group events per session
session_events = df.groupby('user_session')['event_type'].apply(set).reset_index()

# Classify sessions based on event sequence
def classify_session(events):
    if 'purchase' in events and 'cart' in events:
        return 'View + Cart + Purchase'
    elif 'purchase' in events and 'cart' not in events:
        return 'View + Purchase (No Cart)'
    elif 'cart' in events and 'purchase' not in events:
        return 'View + Cart (No Purchase)'
    else:
        return 'Only View'

session_events['session_type'] = session_events['event_type'].apply(classify_session)

# Count session types
funnel_counts = session_events['session_type'].value_counts()
print("Session Types Breakdown:\n", funnel_counts)

# Define stages
total_sessions = funnel_counts.sum()
view_sessions = total_sessions
cart_sessions = funnel_counts.get('View + Cart + Purchase', 0) + funnel_counts.get('View + Cart (No Purchase)', 0)
purchase_sessions = funnel_counts.get('View + Cart + Purchase', 0)  # ✅ Only count purchases that came through cart

# Conversion rates
view_to_cart_rate = cart_sessions / view_sessions * 100
cart_to_purchase_rate = purchase_sessions / cart_sessions * 100 if cart_sessions else 0
view_to_purchase_rate = purchase_sessions / view_sessions * 100

print(f"\nView to Cart Rate: {view_to_cart_rate:.2f}%")
print(f"Cart to Purchase Rate: {cart_to_purchase_rate:.2f}%")
print(f"View to Purchase Rate: {view_to_purchase_rate:.2f}%")

# Create output folder
os.makedirs("charts", exist_ok=True)

# Plot horizontal bar funnel chart
stages = ['View', 'Cart', 'Purchase']
counts = [view_sessions, cart_sessions, purchase_sessions]

plt.figure(figsize=(8, 5))
bars = plt.barh(stages, counts, color='skyblue')

# Annotate values on bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1000, bar.get_y() + bar.get_height()/2, f'{int(width):,}', va='center', fontsize=10)

plt.title("User Funnel: View → Cart → Purchase (Only Cart-based Purchases)")
plt.xlabel("Number of Sessions")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.savefig("charts/funnel_bar_horizontal.png")
plt.show()

# Drop-off calculations
view_to_cart_drop = (view_sessions - cart_sessions) / view_sessions * 100
cart_to_purchase_drop = (cart_sessions - purchase_sessions) / cart_sessions * 100 if cart_sessions else 0

print("\n--- Drop-off Analysis ---")
print(f"Drop-off after View (did not add to cart): {view_to_cart_drop:.2f}%")
print(f"Drop-off after Cart (did not purchase): {cart_to_purchase_drop:.2f}%")
