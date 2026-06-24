CREATE TABLE dim_fund(

amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT,
risk_category TEXT

);

CREATE TABLE fact_nav(

amfi_code INTEGER,
date DATE,
nav REAL,

FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_transactions(

investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,

FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_performance(

amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
expense_ratio_pct REAL,

FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_aum(

fund_house TEXT,
date DATE,
aum_crore REAL

);