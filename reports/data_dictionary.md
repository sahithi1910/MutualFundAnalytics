# Mutual Fund Analytics Data Dictionary

## Fund Master

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique scheme identifier |
| fund_house | Text | Asset Management Company |
| scheme_name | Text | Mutual Fund Scheme Name |
| category | Text | Equity / Debt |
| sub_category | Text | Large Cap, Small Cap etc |
| risk_category | Text | Risk Level |

---

## NAV History

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## Investor Transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor Identifier |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Investment Amount |

---

## Scheme Performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| expense_ratio_pct | Float | Fund Expense Ratio |

---

## AUM

| Column | Type | Description |
|----------|----------|----------|
| fund_house | Text | AMC Name |
| aum_crore | Float | Assets Under Management |