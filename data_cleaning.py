import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("="*60)
print("DAY 2 DATA CLEANING")
print("="*60)

# --------------------------------------------------
# 01 FUND MASTER
# --------------------------------------------------

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

fund_master.drop_duplicates(inplace=True)

fund_master.to_csv(
    "data/processed/cleaned_01_fund_master.csv",
    index=False
)

# --------------------------------------------------
# 02 NAV HISTORY
# --------------------------------------------------

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.drop_duplicates(inplace=True)

nav.to_csv(
    "data/processed/cleaned_02_nav_history.csv",
    index=False
)

# --------------------------------------------------
# 03 AUM
# --------------------------------------------------

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.drop_duplicates(inplace=True)

aum.to_csv(
    "data/processed/cleaned_03_aum_by_fund_house.csv",
    index=False
)

# --------------------------------------------------
# 04 SIP INFLOWS
# --------------------------------------------------

sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip.drop_duplicates(inplace=True)

sip.to_csv(
    "data/processed/cleaned_04_monthly_sip_inflows.csv",
    index=False
)

# --------------------------------------------------
# 05 CATEGORY INFLOWS
# --------------------------------------------------

category = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

category.drop_duplicates(inplace=True)

category.to_csv(
    "data/processed/cleaned_05_category_inflows.csv",
    index=False
)

# --------------------------------------------------
# 06 FOLIO COUNT
# --------------------------------------------------

folio = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio.drop_duplicates(inplace=True)

folio.to_csv(
    "data/processed/cleaned_06_industry_folio_count.csv",
    index=False
)

# --------------------------------------------------
# 07 SCHEME PERFORMANCE
# --------------------------------------------------

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

anomalies = performance[
    (performance["expense_ratio_pct"] < 0.1)
    |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies")
print(anomalies)

performance.to_csv(
    "data/processed/cleaned_07_scheme_performance.csv",
    index=False
)

# --------------------------------------------------
# 08 INVESTOR TRANSACTIONS
# --------------------------------------------------

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.upper()
)

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    "data/processed/cleaned_08_investor_transactions.csv",
    index=False
)

# --------------------------------------------------
# 09 PORTFOLIO HOLDINGS
# --------------------------------------------------

portfolio = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

portfolio.drop_duplicates(inplace=True)

portfolio.to_csv(
    "data/processed/cleaned_09_portfolio_holdings.csv",
    index=False
)

# --------------------------------------------------
# 10 BENCHMARK INDICES
# --------------------------------------------------

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark.drop_duplicates(inplace=True)

benchmark.to_csv(
    "data/processed/cleaned_10_benchmark_indices.csv",
    index=False
)

print("\nAll cleaned files saved successfully.")