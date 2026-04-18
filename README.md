# Customer-Engagement-Product-Utilization-Analytics

## 📌 Project Overview
This project explores **customer churn** in the banking sector using Python‑based analytics and visualization. The goal was to identify how engagement, product depth, and financial commitment influence retention, and to highlight practical strategies for reducing churn.

The analysis was executed in a **Jupyter Notebook**, allowing for iterative validation, classification, and visualization of customer data. Figures and charts were generated using **Seaborn** and **Matplotlib**, with a focus on clarity and stakeholder‑friendly presentation.

---

## 🎯 Objectives
- Evaluate the relationship between engagement and churn.
- Measure retention impact of product count and product mix.
- Identify disengaged yet high‑value customers.
- Support engagement‑driven retention strategies with clear KPIs.

---

## 🔍 Methodology
- **Data Validation:** Checked for missing values, duplicates, and consistency in churn labels.  
- **Engagement Profiles:** Classified customers into categories (active engaged, inactive disengaged, inactive high‑balance, etc.).  
- **Churn Analysis:** Measured churn across product depth, activity status, balance thresholds, credit card ownership, and relationship strength tiers.  
- **Visualization:** Inline charts with whole‑number percentages, decluttered legends, and labels above bars for readability.  

---

## 📊 Key Findings
During this project execution, I found out that:

1. **Product Depth Matters**  
   - Single‑product customers churned at ~28%, while multi‑product customers churned at ~13%.  
   - Bundling products strengthens loyalty and reduces churn.

2. **Engagement Outweighs Wealth**  
   - Active customers churned at <10%.  
   - Inactive high‑balance customers churned at >30%.  
   - Financial value alone does not guarantee retention.

3. **Premium Customers Are at Risk**  
   - Inactive customers with balances >100,000 churned at ~33%, compared to ~20% overall.  
   - These customers require targeted retention campaigns.

4. **Sticky Profiles Are Resilient**  
   - Sticky customers churned at ~9%, while non‑sticky profiles churned at ~21%.  
   - Combining behavioral and financial indicators creates a reliable definition of loyalty.

5. **Engagement Thresholds Provide Benchmarks**  
   - Customers with ≥2 products churned at ~13%.  
   - Inactive members churned at ~27%.  
   - Thresholds help flag customers for proactive engagement.

---

## 📈 KPIs Developed
- Engagement Retention Ratio  
- Product Depth Index  
- High‑Balance Disengagement Rate  
- Credit Card Stickiness Score  
- Relationship Strength Index  

These KPIs provide a practical dashboard for monitoring retention health.

---

## ✅ Conclusion
The project highlights that **engagement and relationship strength are stronger predictors of retention than financial value alone**. Banks should focus on product bundling, engagement campaigns, and identifying sticky profiles to reduce churn.  

This analysis demonstrates how even intermediate‑level Python analytics, when presented clearly, can yield actionable insights for stakeholders.

---

## 📚 References
1. Arefin, S. et al. (2024). *Enhancing Bank Consumer Retention: A Comprehensive Analysis of Churn Prediction Using Machine-Learning and Deep Learning Techniques.* Springer.  
2. IEEE Xplore (2024). *Customer Retention in Banking: Utilizing AI and Machine Learning for Predictive Insights.*  
3. Academia.edu (2024). *Bank Customer Churn Analysis Using Machine Learning Frameworks.*  

---

## ⚙️ Tech Stack
- Python (pandas, numpy, seaborn, matplotlib)  
- Jupyter Notebook  
- CSV data ingestion and validation  

---

## How to run

- Clone this repository :
  git clone https://github.com/Jitin14/Customer-Engagement-Product-Utilization-Analytics.git

- Install dependencies:

pip install -r requirements.txt

- Launch Jupyter Notebook:

   jupyter notebook
- Open the notebook located at:

   ../Notebook/European Bank.ipynb
  Run the cells sequentially to reproduce the analysis.

Or, if you want to explore the interactive dashboard:

streamlit run app.py

