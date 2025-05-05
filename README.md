# E-Commerce User Behavior Analysis

This project analyzes over 40 million user interaction records from a multi-category e-commerce store.  
It explores how users move from product view to cart to purchase — and where they drop off or convert.

---

## Key Analyses

### 1. Funnel Conversion
Tracks user journey stages (View → Cart → Purchase), including session classification and conversion/drop-off rates.

- `funnel_analysis.py`
- Outputs:
  - `charts/funnel_bar_horizontal.png`
  - `charts/funnel_pie_with_legend.png`

### 2. Time-Based Behavior
Calculates how long it takes users to move from view to cart or purchase.

- `session_time_analysis.py`
- Outputs:
  - `charts/time_to_cart_distribution.png`
  - `charts/time_to_purchase_distribution.png`
  - `charts/view_to_cart_vs_purchase.png`

### 3. Views vs Purchases & Conversion Rate
Analyzes product categories by views, purchases, and conversion percentages.

- `view_vs_purchase.py`
- Output:
  - `charts/views_vs_purchases_with_conversion.png`

### 4. Category Insights
Identifies top purchased product categories.

- `category_analysis.py`
- Output:
  - `charts/top10_categories_purchase.png`

### 5. Daily Purchase Trends
Visualizes daily purchase activity in October and November 2019.

- `daily_purchase_trend.py`
- Output:
  - `charts/daily_purchases_trend.png`

---

## Key Insights

- Cart actions are taken faster and more impulsively than purchases.
- Over 80% of purchases happen within 10 minutes of viewing a product.
- ~96% of sessions never go beyond viewing, suggesting a large funnel drop-off.
- Once users add to cart, the chance of purchase is high (~55%).

Detailed insights available in [`insights.md`](insights.md)

---

## Project Structure

| File | Description |
|------|-------------|
| `load_data.py` | Shared data loading function |
| `funnel_analysis.py` | Funnel session classification and drop-off metrics |
| `session_time_analysis.py` | Time from view to cart/purchase and comparison |
| `view_vs_purchase.py` | Category-level views, purchases, and conversion |
| `category_analysis.py` | Top purchased categories |
| `daily_purchase_trend.py` | Daily trend of purchases |
| `EDA.ipynb` | Exploratory data analysis notebook (optional) |
| `run_all.py` | Run all scripts at once |
| `charts/` | Output visualizations |
| `README.md` | Project overview |
| `insights.md` | Written interpretation of key findings |

---

## Dataset

- Source: [Kaggle – E-Commerce Behavior Data from Multi Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
