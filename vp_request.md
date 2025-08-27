<p align="center">
  <img src="repo_files/dark_logo_banner.png" width="1000"/>
  <br>
  <em>A Case Study in E-commerce Sales & Returns Analysis</em>
</p>

<p align="center">
  <img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-complete-brightgreen">
  <img alt="Python" src="https://img.shields.io/badge/python-3.9-blue.svg">
  <img alt="DB" src="https://img.shields.io/badge/database-SQLite-orange.svg">
</p>

## 📦 Scenario: Ecommerce Diagnostic Request from the VP of Sales


## 🧭 Background

After completing its first full year of operations, our ecommerce startup has entered Q3 2025 with strong top-line momentum — but deeper concerns are emerging. While order volume has steadily increased and customer acquisition remains healthy, return rates have not improved, and profitability continues to be eroded by high refund activity and uneven customer value.  

With a full year of sales, returns, and customer behavior now available, leadership is turning its attention toward strategic optimization. The **VP of Sales** has requested a comprehensive diagnostic review and dashboard to surface patterns, risks, and opportunities hidden in our operational data.

This initiative will lay the foundation for data-driven strategy going into the next quarter and year of operations, with an emphasis on identifying which customers, channels, products, and operational practices are helping — or hurting — the bottom line.

### Key Stakeholders

**Position:** VP of Sales  
**Objective:** Improve revenue retention and reduce operational drag caused by returns and inconsistent customer value.

<details>
<summary>🎯 Objectives</summary>

**Develop a SQL-powered diagnostic report and dashboard to:**

- Identify products with high return rates and possible quality issues
- Segment customers by loyalty tier and lifetime value (CLV)
- Analyze regional and channel performance
- Evaluate if expedited shipping is increasing return likelihood
- Highlight patterns by signup cohort and return reason

</details>

<details>

<summary>🧩 Available Data</summary>

The diagnostic will be powered by a simulated ecommerce dataset with the following tables:

- `orders`: Includes region, total, channel, shipping, and customer metadata
- `order_items`: Product-level detail for each order
- `returns`: One row per return with refunded amount and reason
- `return_items`: Line-level detail of items returned
- `customers`: Demographics, signup date, loyalty tier
- `product_catalog`: Name, category, pricing information

</details>

<details>

<summary>🛠️ Key Metrics</summary>

The report will focus on:

- **Top Returned Products** (by count and rate)
- **High Refund Customers** (total refunded $)
- **Regional Sales vs. Returns**
- **Customer Lifetime Value (CLV)** bands
- **Return Rates by Shipping Speed**
- **Return Reasons Breakdown**

</details>

<details>

<summary>📝 Note on Data Source:</summary>
The scenario and dataset used in this analysis were generated using the open-source ecommerce_data_generator project on GitHub. While the data is fully simulated, it reflects realistic e-commerce behavior through the use of structured generation logic.

</details>

<details>

<summary>✍️ Analytical Framing:</summary>
The business context, stakeholder roles, and scenario narrative were crafted using GPT-4 to simulate a real-world diagnostic request. This framing is intended to guide exploratory data analysis, storytelling, and portfolio-quality project design.

</details>

</details>

[← Back to Main README](README.md)