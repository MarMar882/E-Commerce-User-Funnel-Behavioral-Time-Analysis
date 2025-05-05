import pandas as pd
import matplotlib.pyplot as plt
import os
from load_data import load_combined_data

# Load data
df = load_combined_data(nrows=200000)  # optional sample for faster load

# Clean
df = df.dropna(subset=['category_code'])

# Count views & purchases
views_by_cat = df[df['event_type'] == 'view']['category_code'].value_counts()
purchases_by_cat = df[df['event_type'] == 'purchase']['category_code'].value_counts()

# Top categories by purchase
top_categories = purchases_by_cat.nlargest(10).index
views = views_by_cat[top_categories]
purchases = purchases_by_cat[top_categories]
conversion_rate = (purchases / views * 100).round(1)

# Plot
os.makedirs("charts", exist_ok=True)
plt.figure(figsize=(14, 6))
bar_width = 0.4
x = range(len(top_categories))

plt.bar(x, views, width=bar_width, label='Views', color='skyblue')
plt.bar([i + bar_width for i in x], purchases, width=bar_width, label='Purchases', color='mediumseagreen')

# Add conversion %
for i, cat in enumerate(top_categories):
    x_pos = i + bar_width / 2
    cr = conversion_rate[cat]
    plt.text(x_pos, max(views[cat], purchases[cat]) + 1000, f'{cr}%', ha='center', fontsize=10, fontweight='bold')

plt.xticks([i + bar_width / 2 for i in x], top_categories, rotation=45, ha='right')
plt.xlabel("Category")
plt.ylabel("Number of Events")
plt.title("Views vs Purchases per Category (with Conversion %)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("charts/views_vs_purchases_with_conversion.png")
plt.show()
