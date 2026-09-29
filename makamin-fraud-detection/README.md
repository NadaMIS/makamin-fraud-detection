# MAKĀMIN | مكامن — Uncovering Hidden Fraud Patterns

![MAKĀMIN](media/figures/makamin_banner.jpg)

**Financial fraud detection with network analysis.** A Data Science Capstone project (Group 8) that asks one question:

> Is a fraudulent transaction just one transaction, or is it connected to others?

**Team:** Nada Aljaafari · Lujain Alqarni · Alia AlGhamdi · Remas Almutairi

---

## Highlights

| | |
|---|---|
| **Final model** | XGBoost with five historical relationship features |
| **Average Precision** | **0.521** (random guess: 0.034) |
| **ROC-AUC** | **0.909** |
| **Fraud caught at 0.50 threshold** | **74%** (3,014 of 4,064) |
| **Evaluation** | Chronological split: newest 118,108 transactions held out |
| **Dashboard** | MAKĀMIN Streamlit app: risk score → SHAP reasons → 24-hour network |

🎬 **Showcase video:** [`media/MAKAMIN_Showcase_Video.mp4`](media/MAKAMIN_Showcase_Video.mp4)

---

## The problem

Fraud is often coordinated: the same card, address, email domain or device is reused across many transactions. Each one can look normal on its own. In the data we found **35 fraudulent transactions linked to one card and one address within 73 hours**.

![Largest linked fraud group](media/figures/largest_fraud_group_network.png)

## Data

[IEEE-CIS Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection/data) (IEEE-CIS & Vesta Corporation, 2019): 590,540 labelled e-commerce transactions, 3.5% fraud, 434 columns after merging the transaction and identity tables.

> The dataset is **not included** in this repository. Download it from Kaggle (competition rules apply) and run the notebook on Kaggle or locally.

## Approach

1. **Chronological split:** oldest 80% for training, newest 20% for validation, so the model never learns from the future.
2. **Training-only preprocessing:** drop features more than 95% empty, encode categories using training data only, weight fraud 27.5× for class imbalance.
3. **Exploratory fraud network:** fraudulent transactions linked by card + address within 24 hours (exploratory only, since it uses labels).
4. **Five label-free relationship features:** for each transaction, how many *earlier* transactions in the last 24 hours share its card, address, email domain, device, or card + address. A notebook check confirms time order and that no fraud labels are used.
5. **Model comparison:** XGBoost and a neural network (ANN), each with and without the new features. GraphSAGE and RGCN were also tried and did not beat XGBoost.
6. **Explainability:** SHAP on 5,000 validation transactions.
7. **Dashboard:** MAKĀMIN for transaction-level investigation.

## Results

| Model | Average Precision | ROC-AUC |
|---|---|---|
| **XGBoost + historical features** | **0.521** | **0.909** |
| XGBoost baseline | 0.519 | 0.908 |
| ANN baseline | 0.451 | 0.861 |
| ANN + historical features | 0.440 | 0.873 |
| Random guess | 0.034 | 0.500 |

The alert threshold is a business choice: lower thresholds catch more fraud but raise more false alerts.

![Threshold trade-off](media/figures/threshold_tradeoff.png)

## MAKĀMIN dashboard

For a selected validation transaction, MAKĀMIN shows:

1. **Risk score:** the XGBoost fraud probability and decision at the 0.50 reference threshold.
2. **Why:** the top 10 SHAP contributions pushing the score toward or away from fraud.
3. **Who's connected:** earlier transactions from the previous 24 hours that share its card, address, email domain or device, as an interactive network.

| Risk assessment | 24-hour relationship network |
|---|---|
| ![Risk](media/figures/dashboard_risk.jpg) | ![Network](media/figures/dashboard_network.jpg) |

A link between transactions is **investigation context, not proof** of coordinated fraud. MAKĀMIN is a demonstration tool, not a production system.

## Repository structure

```
├── notebooks/
│   └── makamin-graph-based-fraud-detection.ipynb   # full pipeline (EDA → models → SHAP → dashboard assets)
├── app/
│   └── app.py                                      # MAKĀMIN Streamlit dashboard
├── reports/
│   ├── MAKAMIN_Project_Report.pdf
│   └── MAKAMIN_Project_Report.docx
├── presentation/
│   └── MAKAMIN_Presentation.pptx
├── media/
│   ├── MAKAMIN_Showcase_Video.mp4
│   └── figures/
├── requirements.txt
└── README.md
```

## How to run

**1. Notebook.** Open `notebooks/makamin-graph-based-fraud-detection.ipynb` on Kaggle with the IEEE-CIS competition data attached (the notebook reads from `/kaggle/input/competitions/ieee-fraud-detection`). Running it end to end trains the models and exports `dashboard_assets.pkl`.

**2. Dashboard.** Place `dashboard_assets.pkl` next to `app/app.py`, then:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Limitations and future work

- The gain from relationship features is small (+0.0017 AP) and comes from one split. Time-based cross-validation would confirm it.
- Many top features are anonymised, which limits business interpretation.
- `card1` and `addr1` are not true customer IDs.
- The GraphSAGE and RGCN experiments are not included in the final notebook.
- Next steps: richer entity graphs for GNNs, cost-based threshold selection, and hosting MAKĀMIN permanently.

## References

- Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD '16*.
- IEEE-CIS & Vesta Corporation. (2019). *IEEE-CIS Fraud Detection* [Dataset]. Kaggle.
- Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *NeurIPS 30*.
