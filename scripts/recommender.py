import pandas as pd

# Load performance data
performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# -----------------------------------
# Create Risk Appetite Categories
# -----------------------------------

def assign_risk(std_dev):

    if std_dev < 10:
        return "Low"

    elif std_dev < 20:
        return "Moderate"

    else:
        return "High"


performance['risk_appetite'] = (
    performance['std_dev_ann_pct']
    .apply(assign_risk)
)

# -----------------------------------
# User Input
# -----------------------------------

print("\nRisk Options:")
print("Low")
print("Moderate")
print("High")

risk = input(
    "\nEnter Risk Appetite: "
).strip().title()

# -----------------------------------
# Recommendations
# -----------------------------------

recommendations = (
    performance[
        performance['risk_appetite'] == risk
    ]
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            'scheme_name',
            'fund_house',
            'risk_appetite',
            'sharpe_ratio',
            'return_3yr_pct'
        ]
    ].to_string(index=False)
)