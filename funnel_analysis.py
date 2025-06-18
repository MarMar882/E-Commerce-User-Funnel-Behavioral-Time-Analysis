import pandas as pd
import matplotlib.pyplot as plt
import os
from load_data import load_combined_data  # Assumes load_combined_data is defined separately

# ----------------------------
# Compute funnel conversion rates
# ----------------------------
def compute_funnel_rates(df):
    df = df[['user_session', 'event_type']].drop_duplicates()
    session_events = df.groupby('user_session')['event_type'].apply(set).reset_index()

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

    funnel_counts = session_events['session_type'].value_counts()
    total_sessions = funnel_counts.sum()
    view_sessions = total_sessions
    cart_sessions = funnel_counts.get('View + Cart + Purchase', 0) + funnel_counts.get('View + Cart (No Purchase)', 0)
    purchase_sessions = funnel_counts.get('View + Cart + Purchase', 0)

    rates = {
        'view_to_cart': round(cart_sessions / view_sessions * 100, 2),
        'cart_to_purchase': round(purchase_sessions / cart_sessions * 100, 2) if cart_sessions else 0,
        'view_to_purchase': round(purchase_sessions / view_sessions * 100, 2),
        'counts': {
            'View': view_sessions,
            'Cart': cart_sessions,
            'Purchase': purchase_sessions
        },
        'dropoffs': {
            'view_to_cart': round((view_sessions - cart_sessions) / view_sessions * 100, 2),
            'cart_to_purchase': round((cart_sessions - purchase_sessions) / cart_sessions * 100, 2) if cart_sessions else 0
        },
        'raw_counts': funnel_counts
    }

    return rates

# ----------------------------
# Plot funnel as horizontal bar chart
# ----------------------------
def plot_funnel(counts, save_path="charts/funnel_bar_horizontal.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    stages = ['View', 'Cart', 'Purchase']
    values = [counts['View'], counts['Cart'], counts['Purchase']]

    plt.figure(figsize=(8, 5))
    bars = plt.barh(stages, values, color='skyblue')

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1000, bar.get_y() + bar.get_height()/2, f'{int(width):,}', va='center', fontsize=10)

    plt.title("User Funnel: View → Cart → Purchase")
    plt.xlabel("Number of Sessions")
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.savefig(save_path)
    plt.show()

# ----------------------------
# Execution
# ----------------------------

df_all = load_combined_data(nrows=200000)
rates = compute_funnel_rates(df_all)

print("Session Types Breakdown:\n", rates['raw_counts'])

print(f"\nView to Cart Rate: {rates['view_to_cart']}%")
print(f"Cart to Purchase Rate: {rates['cart_to_purchase']}%")
print(f"View to Purchase Rate: {rates['view_to_purchase']}%")

plot_funnel(rates['counts'])

print("\n--- Drop-off Analysis ---")
print(f"Drop-off after View: {rates['dropoffs']['view_to_cart']}%")
print(f"Drop-off after Cart: {rates['dropoffs']['cart_to_purchase']}%")
