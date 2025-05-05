import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from load_data import load_combined_data

df = load_combined_data(nrows=1000000)
df = df.sort_values(by=['user_session', 'event_time'])

# View to Purchase
df_vp = df[df['event_type'].isin(['view', 'purchase'])]
first_view_vp = df_vp[df_vp['event_type'] == 'view'].groupby('user_session')['event_time'].min()
first_purchase = df_vp[df_vp['event_type'] == 'purchase'].groupby('user_session')['event_time'].min()
vp_times = pd.DataFrame({'view_time': first_view_vp, 'purchase_time': first_purchase}).dropna()
vp_times['minutes'] = (vp_times['purchase_time'] - vp_times['view_time']).dt.total_seconds() / 60

# View to Cart
df_vc = df[df['event_type'].isin(['view', 'cart'])]
first_view_vc = df_vc[df_vc['event_type'] == 'view'].groupby('user_session')['event_time'].min()
first_cart = df_vc[df_vc['event_type'] == 'cart'].groupby('user_session')['event_time'].min()
vc_times = pd.DataFrame({'view_time': first_view_vc, 'cart_time': first_cart}).dropna()
vc_times['minutes'] = (vc_times['cart_time'] - vc_times['view_time']).dt.total_seconds() / 60

# Plot both on same chart
plt.figure(figsize=(12, 6))
sns.kdeplot(vc_times['minutes'], label='View to Cart', fill=True, alpha=0.4, linewidth=2, color='steelblue')
sns.kdeplot(vp_times['minutes'], label='View to Purchase', fill=True, alpha=0.4, linewidth=2, color='seagreen')

plt.title("Comparison: Time to Cart vs Time to Purchase")
plt.xlabel("Minutes from First View")
plt.ylabel("Density")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()

os.makedirs("charts", exist_ok=True)
plt.savefig("charts/view_to_cart_vs_purchase.png")
plt.show()

