📊 Food Marketing Analytics — Customer Segmentation

End-to-end marketing analytics project focused on customer value segmentation and data-driven targeting decisions, built using a reproducible Python analytics pipeline.

🚀 Why This Project

Marketing teams often run blanket campaigns without knowing:

💰 Who actually drives revenue

🛒 Which products and channels matter most

🎯 Which customers should (or should not) be targeted

This project solves that problem using EDA + customer segmentation to support segment-based marketing decisions.

🧠 What I Did (Quick Scan)

✅ Cleaned and engineered customer features (Age, Total Spend, Recency, Household)

✅ Performed focused Exploratory Data Analysis (EDA)

✅ Segmented customers using K-Means clustering

✅ Translated clusters into business-ready personas

✅ Generated clear visualizations for decision-makers

📊 Exploratory Data Analysis (EDA)

All figures below are generated programmatically by the Python pipeline and saved automatically.

1️⃣ Customer Value Distribution
<p align="center"> <img src="figures/numeric_distributions.png" width="700"> </p> <p align="center"><i>Income and total spend are right-skewed, indicating strong concentration of customer value.</i></p>

Insight:
A small portion of customers contributes disproportionately to revenue, justifying segmentation over average-based analysis.

2️⃣ Product Category Revenue Drivers
<p align="center"> <img src="figures/avg_spend_products.png" width="700"> </p> <p align="center"><i>Wines and meat products dominate total customer spending.</i></p>

Insight:
Premium product categories drive most revenue, highlighting opportunities for targeted upsell and cross-sell strategies.

3️⃣ Channel Usage Patterns
<p align="center"> <img src="figures/channel_usage.png" width="650"> </p> <p align="center"><i>Store and web channels account for the majority of customer transactions.</i></p>

Insight:
Marketing effectiveness depends heavily on channel strategy rather than uniform outreach.

🧩 Customer Segmentation
4️⃣ Income vs Total Spend (K-Means Clusters)
<p align="center"> <img src="figures/segments_income_spend.png" width="700"> </p> <p align="center"><i>Clear separation between high-value, mid-value, and low-value customer segments.</i></p>

Insight:
Customer segments are visually distinct, validating the clustering approach and confirming meaningful differences in value.

5️⃣ Campaign Response vs Spend
<p align="center"> <img src="figures/spend_vs_response.png" width="650"> </p> <p align="center"><i>Customers who respond to campaigns consistently exhibit higher total spend.</i></p>

Insight:
Campaign responsiveness correlates strongly with customer value, reinforcing the importance of targeted marketing.

🧩 Customer Segments Identified
Segment	Business Meaning
⭐ High-Value Loyalists	Core revenue drivers; high income & high spend
🚀 Aspirational Spenders	Mid-value, promotion-sensitive customers
📱 Convenience-Oriented Shoppers	Under-monetized segment with strong growth potential
🧊 Low-Value / Entry Customers	Low spend; low marketing ROI

✔ Clusters are statistically distinct and business-interpretable.

📌 Business Recommendations

🎯 Prioritize High-Value Loyalists for retention and premium campaigns

📈 Grow Convenience-Oriented Shoppers via personalization and nudges

🎁 Target Aspirational Spenders selectively with promotions

🚫 Suppress costly campaigns for Low-Value / Entry Customers

🛠️ Tech Stack

🐍 Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

📦 Modular project structure (src/, reproducible pipeline)

🌟 Why This Project Stands Out

✔ Business-first problem framing
✔ Clean, production-style analytics pipeline
✔ Visual validation of insights
✔ Focus on actionable decisions, not just models

🔮 Future Enhancements

Campaign ROI optimization

Profit-based targeting strategies

Power BI executive dashboard

Customer lifetime value (CLV) modeling


👤 Author

Anuj Upadhyay

LinkedIn: https://www.linkedin.com/in/anuj-upadhyay-1b040b29/

GitHub: https://github.com/GitAnuj13

Email: anuj.1526@gmail.com

⭐ If you find this project useful, consider giving it a star!
