import pandas as pd

files = {
    "Fund Master": "data/raw/01_fund_master.csv",
    "NAV History": "data/raw/02_nav_history.csv",
    "AUM By Fund House": "data/raw/03_aum_by_fund_house.csv",
    "Monthly SIP Inflows": "data/raw/04_monthly_sip_inflows.csv",
    "Category Inflows": "data/raw/05_category_inflows.csv",
    "Industry Folio Count": "data/raw/06_industry_folio_count.csv",
    "Scheme Performance": "data/raw/07_scheme_performance.csv",
    "Investor Transactions": "data/raw/08_investor_transactions.csv",
    "Portfolio Holdings": "data/raw/09_portfolio_holdings.csv",
    "Benchmark Indices": "data/raw/10_benchmark_indices.csv"
}

datasets = {}

print("=" * 60)
print("MUTUAL FUND ANALYTICS PLATFORM - DATA INGESTION")
print("=" * 60)

for name, path in files.items():

    df = pd.read_csv(path)

    datasets[name] = df

    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

fund_master = datasets["Fund Master"]
nav_history = datasets["NAV History"]

nav_history["date"] = pd.to_datetime(nav_history["date"])

print("\n" + "=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Grades:")
print(fund_master["risk_category"].unique())

print("\nUnique AMFI Codes:")
print(fund_master["amfi_code"].nunique())

print("\nAMFI Uniqueness Check:")

if fund_master["amfi_code"].is_unique:
    print("SUCCESS: Every AMFI code uniquely identifies a scheme.")
else:
    print("WARNING: Duplicate AMFI codes found.")

print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

if len(missing_codes) == 0:
    print("SUCCESS: All AMFI codes exist in NAV History.")
else:
    print("Missing Codes:")
    print(missing_codes)

print("\nDATA INGESTION COMPLETED SUCCESSFULLY")