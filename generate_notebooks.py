import nbformat as nbf

# 03_EDA
nb_eda = nbf.v4.new_notebook()
cells_eda = [
    nbf.v4.new_markdown_cell("# 03 Exploratory Data Analysis (EDA)\nThis notebook explores the cleaned dataset to identify key patterns, trends, and relationships to answer: **How can management increase sales, profit margin, and stock efficiency?**"),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport warnings\n\nwarnings.filterwarnings('ignore')\n\n# Configure visualizations\nplt.style.use('seaborn-v0_8-whitegrid')\nsns.set_palette('muted')\n\ndf = pd.read_csv('data/processed/cleaned_dataset.csv')\ndf['order_date'] = pd.to_datetime(df['order_date'])\ndf['ship_date'] = pd.to_datetime(df['ship_date'])\ndf.head()"),
    nbf.v4.new_markdown_cell("## 1. Univariate Analysis\nUnderstanding the distribution of key numerical and categorical variables."),
    nbf.v4.new_code_cell("fig, axes = plt.subplots(1, 3, figsize=(18, 5))\nsns.histplot(df['sales'], bins=50, kde=True, ax=axes[0], color='blue')\naxes[0].set_title('Sales Distribution')\naxes[0].set_xlim(0, df['sales'].quantile(0.95)) # Cap for visibility\n\nsns.histplot(df['profit'], bins=50, kde=True, ax=axes[1], color='green')\naxes[1].set_title('Profit Distribution')\naxes[1].set_xlim(df['profit'].quantile(0.05), df['profit'].quantile(0.95))\n\nsns.countplot(data=df, x='product_category', ax=axes[2], palette='Set2')\naxes[2].set_title('Orders by Product Category')\nplt.tight_layout()"),
    nbf.v4.new_markdown_cell("## 2. Bivariate Analysis\nAnalyzing the relationships between variables, focusing on drivers of Sales and Profit."),
    nbf.v4.new_code_cell("fig, axes = plt.subplots(1, 2, figsize=(16, 5))\nsns.barplot(data=df, x='region', y='sales', estimator=np.sum, errorbar=None, ax=axes[0], palette='viridis')\naxes[0].set_title('Total Sales by Region')\n\nsns.barplot(data=df, x='region', y='profit', estimator=np.sum, errorbar=None, ax=axes[1], palette='magma')\naxes[1].set_title('Total Profit by Region')\nplt.tight_layout()"),
    nbf.v4.new_code_cell("plt.figure(figsize=(10, 6))\nsns.boxplot(data=df, x='product_category', y='profit', hue='customer_segment', showfliers=False)\nplt.title('Profit Distribution across Categories by Customer Segment')\nplt.show()"),
    nbf.v4.new_markdown_cell("## 3. Time Series Analysis\nExamining seasonality and revenue trends."),
    nbf.v4.new_code_cell("monthly_sales = df.set_index('order_date').resample('ME')['sales'].sum().reset_index()\n\nplt.figure(figsize=(14, 6))\nsns.lineplot(data=monthly_sales, x='order_date', y='sales', marker='o', color='crimson')\nplt.title('Monthly Total Sales Trend')\nplt.xlabel('Date')\nplt.ylabel('Total Sales')\nplt.show()"),
    nbf.v4.new_markdown_cell("## Key Insights from EDA\n1. **Regional Driver**: Certain regions dominate overall sales but might not have proportional profitability.\n2. **Category Performance**: Profitability varies heavily across categories like Furniture vs. Technology.\n3. **Seasonality**: Sales peak during specific times of the year, providing a clear opportunity to minimize inventory stockout.")
]
nb_eda['cells'] = cells_eda

# 04_Statistical_Analysis
nb_stat = nbf.v4.new_notebook()
cells_stat = [
    nbf.v4.new_markdown_cell("# 04 Statistical Analysis\nThis notebook applies statistical techniques, correlation analysis, and hypothesis testing to validate assumptions about margins, discounts, and shipping."),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport scipy.stats as stats\nimport statsmodels.api as sm\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport warnings\n\nwarnings.filterwarnings('ignore')\n\ndf = pd.read_csv('data/processed/cleaned_dataset.csv')"),
    nbf.v4.new_markdown_cell("## 1. Correlation Matrix\nUnderstanding the linear relationships between numerical covariates."),
    nbf.v4.new_code_cell("numeric_cols = ['sales', 'profit', 'discount', 'shipping_cost', 'order_quantity', 'product_base_margin']\ncorrelation_matrix = df[numeric_cols].corr()\n\nplt.figure(figsize=(8, 6))\nsns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)\nplt.title('Correlation Matrix for Numerical Features')\nplt.show()"),
    nbf.v4.new_markdown_cell("## 2. Hypothesis Testing: Discount impact on Profit\n**H0**: Average profit is the same whether discount is < 5% or >= 5%.\n**H1**: Average profit differs based on discount tiers."),
    nbf.v4.new_code_cell("low_discount = df[df['discount'] < 0.05]['profit'].dropna()\nhigh_discount = df[df['discount'] >= 0.05]['profit'].dropna()\n\nt_stat, p_val = stats.ttest_ind(low_discount, high_discount, equal_var=False)\nprint(f'T-Statistic: {t_stat:.4f}')\nprint(f'P-Value: {p_val}')\n\nif p_val < 0.05:\n    print('Reject Null Hypothesis: Significant difference in profit based on discounts.')\nelse:\n    print('Fail to reject Null Hypothesis')"),
    nbf.v4.new_markdown_cell("## 3. Regression Analysis: Predicting Margin\nIs unit price and order quantity significantly predicting base margins?"),
    nbf.v4.new_code_cell("df_valid = df.dropna(subset=['product_base_margin', 'unit_price', 'order_quantity', 'discount'])\nX = df_valid[['unit_price', 'order_quantity', 'discount']]\nY = df_valid['product_base_margin']\nX = sm.add_constant(X) # adding a constant\n\nmodel = sm.OLS(Y, X).fit()\nprint(model.summary())")
]
nb_stat['cells'] = cells_stat

# 05_Final_Load_Prep
nb_final = nbf.v4.new_notebook()
cells_final = [
    nbf.v4.new_markdown_cell("# 05 Final Load Preparation\nAggregating metrics and final dataset preparation to optimize dashboard performance in Tableau."),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport os\n\ndf = pd.read_csv('data/processed/cleaned_dataset.csv')\ndf['order_date'] = pd.to_datetime(df['order_date'])\ndf['ship_date'] = pd.to_datetime(df['ship_date'])\n\n# Ensure calculated columns exist\nif 'gross_profit_margin_pct' not in df.columns:\n    df['gross_profit_margin_pct'] = (df['profit'] / df['sales']) * 100\nif 'shipping_days' not in df.columns:\n    df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days\n"),
    nbf.v4.new_markdown_cell("## 1. Creating the Final Tableau Flat Table\nThe existing dataset is robust. We will save out a designated `tableau_ready.csv` that contains refined business KPIs."),
    nbf.v4.new_code_cell("final_columns = [\n    'order_id', 'order_date', 'order_year', 'order_month',\n    'customer_name', 'customer_segment', 'city', 'state', 'region',\n    'product_category', 'product_sub_category', 'product_name',\n    'sales', 'profit', 'gross_profit_margin_pct', 'order_quantity',\n    'discount', 'shipping_cost', 'shipping_days', 'ship_mode', 'order_priority'\n]\ntableau_df = df[[c for c in final_columns if c in df.columns]]\n\nos.makedirs('data/processed', exist_ok=True)\ntableau_df.to_csv('data/processed/tableau_ready_dataset.csv', index=False)\nprint(f'Exported {tableau_df.shape[0]} rows to tableau_ready_dataset.csv')"),
    nbf.v4.new_markdown_cell("## 2. Aggregate Summaries for Auxiliary Dashboard Data\nProviding grouped datasets if needed for particular mapping or trend optimizations."),
    nbf.v4.new_code_cell("monthly_kpi = tableau_df.groupby(['order_year', 'order_month']).agg({\n    'sales': 'sum',\n    'profit': 'sum',\n    'order_quantity': 'sum'\n}).reset_index()\n\nmonthly_kpi['monthly_revenue_growth_pct'] = monthly_kpi['sales'].pct_change() * 100\nmonthly_kpi.to_csv('data/processed/monthly_kpis.csv', index=False)\nprint('Exported Monthly KPIs')")
]
nb_final['cells'] = cells_final

# Write the notebooks to files
nbf.write(nb_eda, 'notebooks/03_eda.ipynb')
nbf.write(nb_stat, 'notebooks/04_statistical_analysis.ipynb')
nbf.write(nb_final, 'notebooks/05_final_load_prep.ipynb')

print("All analysis notebooks generated successfully.")
