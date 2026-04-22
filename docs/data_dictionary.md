# Data Dictionary – Profit Track

Use this file to document the business-ready retail dataset used for the Profit Track capstone project.

---

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Walmart Retail Dataset |
| Source | Provided capstone retail transactional dataset |
| Raw file name | Walmart-Retail-Dataset.csv |
| Cleaned file name | cleaned_dataset.csv |
| Project Name | Profit Track |
| Rows | 673,502 |
| Columns | 26 |
| Granularity | One row per order transaction |
| Date Range | 2019-01-01 to 2023-01-17 |

---

## Business Objective

Analyze sales, profit margin, and stock efficiency to help management identify the best-performing cities, product categories, customer segments, and sales channels.

---

## Dashboard Decision Question

How can management increase sales, profit margin, and stock efficiency by identifying the best-performing cities, categories, channels, brands, and customer segments?

---

## Expected Insights

- Which locations generate the highest revenue
- Which customer segments are most profitable
- Which product categories drive strong margins
- Which shipping methods increase costs
- Where stock inefficiencies reduce performance
- Seasonal monthly revenue patterns

---

## Target KPIs

| KPI | Definition | Business Value |
|---|---|---|
| Monthly Revenue Growth % | Month-over-month sales growth rate | Measures business expansion |
| Gross Profit Margin % | Profit ÷ Sales × 100 | Measures profitability efficiency |
| Inventory Stockout Rate % | Estimated unavailable stock events ÷ demand | Measures stock efficiency |

---

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| city | string | Customer city | Stevens Point | Geo dashboard | Nulls filled with mode |
| customer_age | float | Customer age | 60 | Segment analysis | Median imputed |
| customer_name | string | Customer name | Dennis Bolton | CRM analysis | Nulls filled |
| customer_segment | string | Segment type | Corporate | KPI filters | Nulls filled |
| discount | float | Discount applied | 0.17 | Margin analysis | Numeric cast |
| order_date | date | Order placed date | 2020-02-29 | Trend analysis | Converted to datetime |
| order_id | string | Unique order ID | UUID | Transaction tracking | Cleaned text |
| order_priority | string | Priority level | High | Ops analysis | Nulls filled |
| order_quantity | float | Quantity ordered | 7 | Demand analysis | Numeric cast |
| product_base_margin | float | Estimated base margin ratio | 0.55 | Margin KPI | Numeric cast |
| product_category | string | Main category | Furniture | Category dashboard | Nulls filled |
| product_container | string | Packaging type | Box | Shipping analysis | Nulls filled |
| product_name | string | Product title | Office Chair | Product ranking | Nulls filled |
| product_sub_category | string | Subcategory | Chairs | Product drilldown | Nulls filled |
| profit | float | Profit earned | 3.29 | Profit KPI | Numeric cast |
| region | string | Sales region | Central | Regional dashboard | Nulls filled |
| sales | float | Revenue amount | 21.84 | Revenue KPI | Numeric cast |
| ship_date | date | Shipping date | 2020-03-02 | Delivery KPI | Converted to datetime |
| ship_mode | string | Delivery method | Delivery Truck | Logistics analysis | Nulls filled |
| shipping_cost | float | Cost of shipping | 3.77 | Cost KPI | Numeric cast |
| state | string | Customer state | Wisconsin | Geo map | Nulls filled |
| unit_price | float | Price per unit | 3.29 | Pricing analysis | Numeric cast |
| zip_code | float | Postal code | 54481 | Mapping | Numeric cast |
| order_year | int | Year from order_date | 2020 | Annual trend | Derived |
| order_month | int | Month from order_date | 2 | Monthly trend | Derived |
| shipping_days | int | Days to deliver | 2 | SLA / delivery KPI | Derived |

---

## Derived Columns

| Derived Column | Logic | Business Meaning |
|---|---|---|
| order_year | YEAR(order_date) | Compare yearly performance |
| order_month | MONTH(order_date) | Detect seasonality |
| shipping_days | ship_date - order_date | Delivery speed efficiency |
| gross_profit_margin_pct | profit / sales × 100 | Profitability KPI |
| monthly_revenue_growth_pct | Current month vs prior month | Growth KPI |

---

## Data Quality Notes

- Missing values were present in multiple columns and were imputed.
- Numeric nulls filled using median values.
- Categorical nulls filled using mode values.
- Duplicate records removed during ETL.
- Date fields standardized to datetime.
- Some region anomalies (example: `40.2`) should be reviewed.
- Zip code stored as numeric due to source format.
- Inventory stockout rate may require proxy logic because direct stock columns are not present.

---

## Stakeholder Decisions Enabled

- Increase sales in high-performing markets
- Improve margin through discount control
- Optimize product mix
- Reduce shipping cost leakage
- Improve customer targeting
- Improve stock planning and replenishment