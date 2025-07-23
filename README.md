# 🧪 A/B Testing Simulator & Conversion Analysis

This project simulates an A/B test to evaluate the performance of two different landing pages in terms of user conversion. The goal is to demonstrate statistical testing, data visualization, and data storytelling in the context of product experimentation.

---

## 📌 Objective

- Simulate and analyze the results of an A/B test using Python
- Perform hypothesis testing to determine statistical significance
- Visualize conversion rates and provide actionable insights
- Package everything into a readable and replicable workflow

---

## 🧰 Tools Used

- Python (Pandas, NumPy, SciPy, Seaborn)
- Excel (for raw data storage)
- Jupyter Notebooks

---

## 📊 Project Summary
Group B showed a 13% conversion rate, compared to Group A's 11%, representing an absolute lift of 2% and a relative lift of 18.18%. A z-test for proportions yielded a p-value of 0.02, indicating the result is statistically significant at the 95% confidence level.
- 20,000 simulated user sessions split between Group A and Group B
- Group B shows a higher conversion rate (~13.66% vs. 10.65%)
- Z-test for proportions shows statistically significant difference (p < 0.05)
- Recommendation: rollout version B
