import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data (sample of 200,000 rows from each month for faster performance)
df_oct = pd.read_csv("2019-Oct.csv", parse_dates=['event_time'], nrows=200000)
df_nov = pd.read_csv("2019-Nov.csv", parse_dates=['event_time'], nrows=200000)
df_all = pd.concat([df_oct, df_nov], ignore_index=True)

# Drop rows with missing category information
df_all = df_all.dropna(subset=['category_code'])

# Count views and purchases per category
views_by_cat = df_all[df_all['event_type'] == 'view']['category_code'].value_counts()
purchases_by_cat = df_all[df_all['event_type'] == 'purchase']['category_code'].value_counts()

# Select top 10 categories by number of purchases
top_categories = purchases_by_cat.nlargest(10).index

# Prepare data
views = views_by_cat[top_categories]
purchases = purchases_by_cat[top_categories]
conversion_rate = (purchases / views * 100).round(1)

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

# Plot bar chart
plt.figure(figsize=(14, 6))
bar_width = 0.4
x = range(len(top_categories))

plt.bar(x, views, width=bar_width, label='Views', color='skyblue')
plt.bar([i + bar_width for i in x], purchases, width=bar_width, label='Purchases', color='mediumseagreen')

# Add conversion rate % as text on top
for i, cat in enumerate(top_categories):
    x_pos = i + bar_width / 2
    cr = conversion_rate[cat]
    plt.text(x_pos, max(views[cat], purchases[cat]) + 1000, f'{cr}%', ha='center', fontsize=10, fontweight='bold')

# Chart formatting
plt.xticks([i + bar_width / 2 for i in x], top_categories, rotation=45, ha='right')
plt.xlabel("Category")
plt.ylabel("Number of Events")
plt.title("Views vs Purchases per Category (with Conversion %)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("charts/views_vs_purchases_with_conversion.png")
plt.show()
