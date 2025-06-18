# Debugging example for compute_funnel_rates

from funnel_analysis import compute_funnel_rates
import pandas as pd

# Create dummy DataFrame to test
data = {
    'user_session': ['s1', 's1', 's2', 's2', 's3'],
    'event_type': ['view', 'cart', 'view', 'purchase', 'view']
}
df_test = pd.DataFrame(data)

# Run function
rates = compute_funnel_rates(df_test)

# Assert expected conversion counts
assert rates['counts']['View'] == 3, "Expected 3 view sessions"
assert rates['counts']['Cart'] == 1, "Expected 1 cart session"
assert rates['counts']['Purchase'] == 1, "Expected 1 purchase session"

print("All debug tests passed.")
