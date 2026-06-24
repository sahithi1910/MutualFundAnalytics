-- Top 5 fund houses by AUM

SELECT fund_house,
MAX(aum_crore)
FROM fact_aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

------------------------------------------------

SELECT
strftime('%Y-%m',date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

------------------------------------------------

SELECT state,
COUNT(*) total_transactions
FROM fact_transactions
GROUP BY state;

------------------------------------------------

SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

------------------------------------------------

SELECT AVG(expense_ratio_pct)
FROM fact_performance;

------------------------------------------------

SELECT amfi_code,
MAX(nav)
FROM fact_nav
GROUP BY amfi_code;

------------------------------------------------

SELECT fund_house,
COUNT(*) schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY schemes DESC;

------------------------------------------------

SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

------------------------------------------------

SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;

------------------------------------------------

SELECT AVG(return_5yr_pct)
FROM fact_performance;