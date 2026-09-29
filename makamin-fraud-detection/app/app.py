# ============================================================
# MAKĀMIN | مكامن
# FRAUD ANALYTICS & INVESTIGATION DASHBOARD
# ============================================================

import os
import html
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

from pyvis.network import Network


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MAKĀMIN | Fraud Investigation",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown("""
<style>

:root {
    --bg: #070A12;
    --panel: #0D1220;
    --panel2: #111827;
    --purple: #8B5CF6;
    --purple2: #A78BFA;
    --cyan: #38BDF8;
    --green: #34D399;
    --red: #FB7185;
    --amber: #FBBF24;
    --text: #F8FAFC;
    --muted: #94A3B8;
}

.stApp {
    background:
        radial-gradient(circle at 12% 4%,
            rgba(139,92,246,.16), transparent 26%),
        radial-gradient(circle at 88% 10%,
            rgba(56,189,248,.09), transparent 24%),
        linear-gradient(180deg, #070A12 0%, #080C15 100%);
    color: var(--text);
}

.block-container {
    max-width: 1480px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 44px;
    border-radius: 28px;
    margin-bottom: 34px;

    background:
        linear-gradient(135deg,
            rgba(139,92,246,.18),
            rgba(56,189,248,.07));

    border: 1px solid rgba(167,139,250,.22);

    box-shadow:
        0 24px 70px rgba(0,0,0,.35),
        inset 0 1px 0 rgba(255,255,255,.05);
}

.hero:after {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    right: -80px;
    top: -100px;
    border-radius: 50%;
    background: rgba(139,92,246,.12);
    filter: blur(10px);
}

.hero-badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(139,92,246,.14);
    border: 1px solid rgba(167,139,250,.28);
    color: #C4B5FD;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 17px;
}

.hero-title {
    font-size: 48px;
    line-height: 1.05;
    font-weight: 850;
    color: #FFFFFF;
    letter-spacing: -1.5px;
}

.hero-tagline {
    margin-top: 9px;
    font-size: 19px;
    color: #C4B5FD;
    font-weight: 700;
}

.hero-text {
    margin-top: 17px;
    max-width: 900px;
    color: #CBD5E1;
    font-size: 15.5px;
    line-height: 1.8;
}

.hero-flow {
    margin-top: 22px;
    color: #94A3B8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .4px;
}


/* ============================================================
   SECTION HEADERS
   ============================================================ */

.section-kicker {
    color: #A78BFA;
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 1.6px;
    margin-bottom: 6px;
}

.section-title {
    color: #F8FAFC;
    font-size: 29px;
    font-weight: 850;
    letter-spacing: -.4px;
    margin-bottom: 8px;
}

.section-desc {
    color: #94A3B8;
    line-height: 1.7;
    margin-bottom: 24px;
    max-width: 1000px;
}


/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    min-height: 142px;
    padding: 20px 20px;
    border-radius: 19px;

    background:
        linear-gradient(145deg,
            rgba(255,255,255,.065),
            rgba(255,255,255,.025));

    border: 1px solid rgba(255,255,255,.085);

    box-shadow:
        0 14px 35px rgba(0,0,0,.20),
        inset 0 1px 0 rgba(255,255,255,.035);

    transition: .2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    border-color: rgba(167,139,250,.25);
}

.kpi-icon {
    font-size: 22px;
    margin-bottom: 12px;
}

.kpi-label {
    color: #94A3B8;
    font-size: 10.5px;
    font-weight: 850;
    letter-spacing: .9px;
    margin-bottom: 7px;
}

.kpi-value {
    color: #F8FAFC;
    font-size: 26px;
    font-weight: 850;
}


/* ============================================================
   PROFILE
   ============================================================ */

.profile-card {
    min-height: 94px;
    padding: 16px 17px;
    border-radius: 15px;

    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.07);
}

.profile-label {
    color: #94A3B8;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: .9px;
    margin-bottom: 8px;
}

.profile-value {
    color: #F8FAFC;
    font-size: 15px;
    font-weight: 750;
    word-break: break-word;
}


/* ============================================================
   SHAP DIRECTION CARDS
   ============================================================ */

.risk-up {
    min-height: 145px;
    padding: 21px 23px;
    border-radius: 18px;

    background:
        linear-gradient(135deg,
            rgba(251,113,133,.14),
            rgba(251,113,133,.035));

    border: 1px solid rgba(251,113,133,.28);
}

.risk-down {
    min-height: 145px;
    padding: 21px 23px;
    border-radius: 18px;

    background:
        linear-gradient(135deg,
            rgba(52,211,153,.14),
            rgba(52,211,153,.035));

    border: 1px solid rgba(52,211,153,.28);
}

.direction-label {
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 1.1px;
    margin-bottom: 13px;
}

.up-label { color: #FDA4AF; }
.down-label { color: #6EE7B7; }

.direction-feature {
    color: #FFFFFF;
    font-size: 20px;
    font-weight: 850;
    margin-bottom: 5px;
}

.direction-value {
    font-size: 17px;
    font-weight: 850;
}

.up-value { color: #FB7185; }
.down-value { color: #34D399; }

.direction-caption {
    color: #94A3B8;
    font-size: 12px;
    margin-top: 8px;
}


/* ============================================================
   INFO CARDS
   ============================================================ */

.explain-card {
    padding: 19px 21px;
    border-radius: 16px;

    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.075);

    color: #CBD5E1;
    line-height: 1.75;

    margin-top: 12px;
    margin-bottom: 16px;
}

.legend-box {
    padding: 12px 14px;
    border-radius: 12px;

    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.07);

    text-align: center;
    color: #CBD5E1;
}

.soft-divider {
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(167,139,250,.38),
            transparent
        );

    margin: 46px 0;
}


/* ============================================================
   SELECT BOX
   ============================================================ */

div[data-baseweb="select"] > div {
    background-color: #101624;
    border-color: rgba(167,139,250,.20);
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer-box {
    margin-top: 50px;
    padding: 28px;
    border-radius: 20px;

    background:
        linear-gradient(135deg,
            rgba(139,92,246,.07),
            rgba(56,189,248,.03));

    border: 1px solid rgba(255,255,255,.07);

    text-align: center;
    color: #94A3B8;
    line-height: 1.9;
}

.footer-brand {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 850;
}

.footer-tagline {
    color: #A78BFA;
    font-weight: 750;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ASSETS_PATH = os.path.join(
    BASE_DIR,
    "dashboard_assets.pkl"
)


@st.cache_resource
def load_dashboard_assets():
    return joblib.load(ASSETS_PATH)


assets = load_dashboard_assets()


overview_data = assets[
    "overview_data"
].copy()

investigation_data = assets[
    "investigation_data"
].copy()

shap_dashboard_data = assets[
    "shap_dashboard_data"
].copy()

graph_connections = assets[
    "graph_connections"
].copy()


overview_data["TransactionID"] = (
    overview_data["TransactionID"].astype(int)
)

investigation_data["TransactionID"] = (
    investigation_data["TransactionID"].astype(int)
)

shap_dashboard_data["TransactionID"] = (
    shap_dashboard_data["TransactionID"].astype(int)
)


if len(graph_connections) > 0:

    graph_connections["Source_Transaction"] = (
        graph_connections[
            "Source_Transaction"
        ].astype(int)
    )

    graph_connections["Related_Transaction"] = (
        graph_connections[
            "Related_Transaction"
        ].astype(int)
    )

    graph_connections = (
        graph_connections
        .set_index(
            "Source_Transaction",
            drop=False
        )
        .sort_index()
    )


# ============================================================
# HELPERS
# ============================================================

def kpi_card(icon, label, value):

    st.markdown(
        f"""
<div class="kpi-card">
<div class="kpi-icon">{icon}</div>
<div class="kpi-label">{label}</div>
<div class="kpi-value">{value}</div>
</div>
""",
        unsafe_allow_html=True
    )


def profile_card(label, value):

    st.markdown(
        f"""
<div class="profile-card">
<div class="profile-label">{label}</div>
<div class="profile-value">{html.escape(str(value))}</div>
</div>
""",
        unsafe_allow_html=True
    )


def clean_value(value):

    if pd.isna(value):
        return "Unavailable"

    return str(value)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">
<div class="hero-badge">FRAUD INTELLIGENCE · EXPLAINABLE AI · RELATIONAL ANALYSIS</div>
<div class="hero-title">MAKĀMIN | مكامن</div>
<div class="hero-tagline">Uncovering Hidden Fraud Patterns</div>
<div class="hero-text">
A fraud analytics and investigation workspace that combines
Enhanced XGBoost risk scoring, local SHAP explanations, and
historical relational evidence to move from population-level
monitoring to individual transaction investigation.
</div>
<div class="hero-flow">
OVERVIEW &nbsp;→&nbsp; DETECT &nbsp;→&nbsp; EXPLAIN
&nbsp;→&nbsp; INVESTIGATE &nbsp;→&nbsp; VISUALIZE
</div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# 01 OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-kicker">01 · OVERALL ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Fraud Detection Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-desc">'
    'A population-level view of Enhanced XGBoost predictions '
    'across the complete chronological validation set.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# METRICS
# ============================================================

total_transactions = len(overview_data)

actual_fraud = int(
    overview_data["Actual_Fraud"].sum()
)

actual_fraud_rate = (
    actual_fraud /
    total_transactions *
    100
)

predicted_fraud = int(
    overview_data["Fraud_Prediction"].sum()
)


true_positive = int(
    (
        (overview_data["Actual_Fraud"] == 1)
        &
        (overview_data["Fraud_Prediction"] == 1)
    ).sum()
)


false_positive = int(
    (
        (overview_data["Actual_Fraud"] == 0)
        &
        (overview_data["Fraud_Prediction"] == 1)
    ).sum()
)


false_negative = int(
    (
        (overview_data["Actual_Fraud"] == 1)
        &
        (overview_data["Fraud_Prediction"] == 0)
    ).sum()
)


true_negative = int(
    (
        (overview_data["Actual_Fraud"] == 0)
        &
        (overview_data["Fraud_Prediction"] == 0)
    ).sum()
)


recall = (
    true_positive /
    (true_positive + false_negative) *
    100
)


precision = (
    true_positive /
    (true_positive + false_positive) *
    100
)


# ============================================================
# KPI ROW
# ============================================================

k1, k2, k3, k4, k5 = st.columns(5)


with k1:
    kpi_card(
        "◈",
        "VALIDATION TRANSACTIONS",
        f"{total_transactions:,}"
    )


with k2:
    kpi_card(
        "◆",
        "KNOWN FRAUD RATE",
        f"{actual_fraud_rate:.2f}%"
    )


with k3:
    kpi_card(
        "◎",
        "MODEL FRAUD ALERTS",
        f"{predicted_fraud:,}"
    )


with k4:
    kpi_card(
        "✓",
        "FRAUD DETECTED",
        f"{true_positive:,}"
    )


with k5:
    kpi_card(
        "↗",
        "RECALL @ 0.50",
        f"{recall:.2f}%"
    )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# OVERVIEW CHARTS
# ============================================================

left_chart, right_chart = st.columns(
    [1.3, 1]
)


# ------------------------------------------------------------
# RISK DISTRIBUTION
# ------------------------------------------------------------

with left_chart:

    st.markdown(
        "#### Risk Score Distribution"
    )

    fig_risk = go.Figure()


    fig_risk.add_trace(
        go.Histogram(
            x=overview_data.loc[
                overview_data[
                    "Actual_Fraud"
                ] == 0,
                "Risk_Score"
            ],

            name="Known Non-Fraud",
            opacity=.72,
            nbinsx=55,

            marker_color="#38BDF8"
        )
    )


    fig_risk.add_trace(
        go.Histogram(
            x=overview_data.loc[
                overview_data[
                    "Actual_Fraud"
                ] == 1,
                "Risk_Score"
            ],

            name="Known Fraud",
            opacity=.78,
            nbinsx=55,

            marker_color="#FB7185"
        )
    )


    fig_risk.add_vline(
        x=.50,
        line_dash="dash",
        line_color="#FBBF24",
        annotation_text="0.50 threshold",
        annotation_font_color="#FBBF24"
    )


    fig_risk.update_layout(
        barmode="overlay",
        height=410,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,.015)",

        xaxis_title="Enhanced XGBoost Risk Score",
        yaxis_title="Transactions",

        legend=dict(
            orientation="h",
            y=1.12
        ),

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )


    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )


# ------------------------------------------------------------
# OUTCOMES
# ------------------------------------------------------------

with right_chart:

    st.markdown(
        "#### Reference-Threshold Outcomes"
    )


    outcome_labels = [
        "Fraud Detected",
        "Fraud Missed",
        "False Alerts"
    ]


    outcome_values = [
        true_positive,
        false_negative,
        false_positive
    ]


    outcome_colors = [
        "#34D399",
        "#FB7185",
        "#FBBF24"
    ]


    fig_outcomes = go.Figure(
        go.Bar(
            x=outcome_labels,
            y=outcome_values,

            marker_color=outcome_colors,

            text=[
                f"{x:,}"
                for x in outcome_values
            ],

            textposition="outside"
        )
    )


    fig_outcomes.update_layout(
        height=410,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,.015)",

        yaxis_title="Transactions",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )


    st.plotly_chart(
        fig_outcomes,
        use_container_width=True
    )


# ============================================================
# EVALUATION CONTEXT
# ============================================================

st.markdown(
    f"""
<div class="explain-card">
<b>Evaluation snapshot</b><br><br>
At the reference threshold of <b>0.50</b>, Enhanced XGBoost
detected <b>{true_positive:,}</b> known fraud transactions,
with <b>{recall:.2f}% recall</b> and
<b>{precision:.2f}% precision</b>.
The threshold is retained as a reference point for model
evaluation and dashboard demonstration; it is not presented
as an optimized production threshold.
</div>
""",
    unsafe_allow_html=True
)


st.markdown(
    '<div class="soft-divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# 02 CASE INVESTIGATION
# ============================================================

st.markdown(
    '<div class="section-kicker">02 · CASE INVESTIGATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Investigate a Transaction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-desc">'
    'Drill down into one of the 5,000 validation transactions '
    'included in the local SHAP investigation sample.'
    '</div>',
    unsafe_allow_html=True
)


available_transactions = (
    investigation_data[
        "TransactionID"
    ].astype(int).tolist()
)


selected_transaction_id = st.selectbox(
    "Select Transaction ID",
    available_transactions,
    index=0
)


selected_row = (
    investigation_data.loc[
        investigation_data[
            "TransactionID"
        ] == selected_transaction_id
    ].iloc[0]
)


risk_score = float(
    selected_row["Risk_Score"]
)

risk_percent = (
    risk_score * 100
)

prediction = int(
    selected_row["Fraud_Prediction"]
)

actual_label = int(
    selected_row["Actual_Fraud"]
)


prediction_text = (
    "Fraud Alert"
    if prediction == 1
    else "No Fraud Alert"
)


actual_text = (
    "Fraud"
    if actual_label == 1
    else "Non-Fraud"
)


# ============================================================
# RISK ASSESSMENT
# ============================================================

st.markdown(
    "### Risk Assessment"
)


risk_left, risk_right = st.columns(
    [1.15, 1.85]
)


# ------------------------------------------------------------
# GAUGE
# ------------------------------------------------------------

with risk_left:

    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=risk_percent,

            number={
                "suffix": "%",
                "font": {
                    "size": 38,
                    "color": "#F8FAFC"
                }
            },

            title={
                "text": "Enhanced XGBoost Risk Score",
                "font": {
                    "size": 15,
                    "color": "#CBD5E1"
                }
            },

            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickcolor": "#64748B"
                },

                "bar": {
                    "color": (
                        "#FB7185"
                        if risk_percent >= 50
                        else "#38BDF8"
                    )
                },

                "bgcolor": "#111827",

                "borderwidth": 0,

                "steps": [
                    {
                        "range": [0, 50],
                        "color": "rgba(52,211,153,.10)"
                    },
                    {
                        "range": [50, 100],
                        "color": "rgba(251,113,133,.12)"
                    }
                ],

                "threshold": {
                    "line": {
                        "color": "#FBBF24",
                        "width": 4
                    },
                    "thickness": .8,
                    "value": 50
                }
            }
        )
    )


    fig_gauge.update_layout(
        height=290,
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=25,
            r=25,
            t=45,
            b=10
        )
    )


    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )


# ------------------------------------------------------------
# RISK CARDS
# ------------------------------------------------------------

with risk_right:

    r1, r2, r3 = st.columns(3)


    with r1:
        kpi_card(
            "ID",
            "TRANSACTION",
            selected_transaction_id
        )


    with r2:
        kpi_card(
            "AI",
            "MODEL DECISION",
            prediction_text
        )


    with r3:
        kpi_card(
            "GT",
            "KNOWN LABEL",
            actual_text
        )


    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="explain-card">
The yellow marker on the gauge represents the
<b>0.50 reference threshold</b>.
The known label is shown because this is validation data;
it would not be available when scoring a new transaction
in deployment.
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# PROFILE
# ============================================================

st.markdown(
    "### Transaction Profile"
)


p1, p2, p3, p4, p5 = st.columns(5)


with p1:
    profile_card(
        "TRANSACTION AMOUNT",
        clean_value(
            selected_row["TransactionAmt"]
        )
    )


with p2:
    profile_card(
        "CARD",
        clean_value(
            selected_row["card1"]
        )
    )


with p3:
    profile_card(
        "ADDRESS",
        clean_value(
            selected_row["addr1"]
        )
    )


with p4:
    profile_card(
        "EMAIL DOMAIN",
        clean_value(
            selected_row["P_emaildomain"]
        )
    )


with p5:
    profile_card(
        "DEVICE",
        clean_value(
            selected_row["DeviceInfo"]
        )
    )


st.markdown(
    '<div class="soft-divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# 03 EXPLAINABILITY
# ============================================================

st.markdown(
    '<div class="section-kicker">03 · EXPLAINABILITY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">What Drove the Risk Score?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-desc">'
    'Local SHAP values reveal which features pushed the model '
    'toward higher fraud risk and which features reduced it.'
    '</div>',
    unsafe_allow_html=True
)


transaction_shap = (
    shap_dashboard_data.loc[
        shap_dashboard_data[
            "TransactionID"
        ] == selected_transaction_id
    ].copy()
)


transaction_shap[
    "Abs_SHAP"
] = transaction_shap[
    "SHAP_Value"
].abs()


# ============================================================
# STRONGEST INCREASE / DECREASE
# ============================================================

positive_shap = (
    transaction_shap.loc[
        transaction_shap[
            "SHAP_Value"
        ] > 0
    ]
    .sort_values(
        "SHAP_Value",
        ascending=False
    )
)


negative_shap = (
    transaction_shap.loc[
        transaction_shap[
            "SHAP_Value"
        ] < 0
    ]
    .sort_values(
        "SHAP_Value",
        ascending=True
    )
)


if len(positive_shap) > 0:

    strongest_up = positive_shap.iloc[0]

    up_feature = html.escape(
        str(
            strongest_up[
                "Feature"
            ]
        )
    )

    up_value = float(
        strongest_up[
            "SHAP_Value"
        ]
    )

else:

    up_feature = "None"
    up_value = 0.0


if len(negative_shap) > 0:

    strongest_down = negative_shap.iloc[0]

    down_feature = html.escape(
        str(
            strongest_down[
                "Feature"
            ]
        )
    )

    down_value = float(
        strongest_down[
            "SHAP_Value"
        ]
    )

else:

    down_feature = "None"
    down_value = 0.0


direction_left, direction_right = st.columns(2)


with direction_left:

    st.markdown(
        f"""
<div class="risk-up">
<div class="direction-label up-label">
▲ FRAUD RISK INCREASE
</div>
<div class="direction-feature">
{up_feature}
</div>
<div class="direction-value up-value">
{up_value:+.3f} SHAP
</div>
<div class="direction-caption">
Strongest displayed feature pushing this prediction
toward higher fraud risk.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with direction_right:

    st.markdown(
        f"""
<div class="risk-down">
<div class="direction-label down-label">
▼ FRAUD RISK DECREASE
</div>
<div class="direction-feature">
{down_feature}
</div>
<div class="direction-value down-value">
{down_value:+.3f} SHAP
</div>
<div class="direction-caption">
Strongest displayed feature pushing this prediction
toward lower fraud risk.
</div>
</div>
""",
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# SHAP BAR CHART
# ============================================================

transaction_shap = (
    transaction_shap
    .sort_values(
        "Abs_SHAP",
        ascending=True
    )
)


shap_colors = [
    "#FB7185"
    if value > 0
    else "#34D399"

    for value in transaction_shap[
        "SHAP_Value"
    ]
]


fig_shap = go.Figure(
    go.Bar(
        x=transaction_shap[
            "SHAP_Value"
        ],

        y=transaction_shap[
            "Feature"
        ],

        orientation="h",

        marker_color=shap_colors,

        text=[
            f"{x:+.3f}"
            for x in transaction_shap[
                "SHAP_Value"
            ]
        ],

        textposition="outside"
    )
)


fig_shap.add_vline(
    x=0,
    line_color="#64748B",
    line_width=1.2
)


fig_shap.update_layout(
    height=490,

    template="plotly_dark",

    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,.015)",

    xaxis_title="SHAP Contribution",
    yaxis_title="",

    showlegend=False,

    margin=dict(
        l=20,
        r=60,
        t=25,
        b=20
    )
)


st.plotly_chart(
    fig_shap,
    use_container_width=True
)


st.markdown(
    """
<div class="explain-card">
<span style="color:#FB7185"><b>Red</b></span>
features push the model toward a higher fraud risk.
&nbsp;&nbsp;
<span style="color:#34D399"><b>Green</b></span>
features push the model toward a lower fraud risk.
<br><br>
SHAP explains the model's local prediction; it does not
establish that an individual feature caused fraud.
</div>
""",
    unsafe_allow_html=True
)


st.markdown(
    '<div class="soft-divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# 04 RELATIONAL INVESTIGATION
# ============================================================

st.markdown(
    '<div class="section-kicker">04 · RELATIONAL INVESTIGATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Historical Transaction Network</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-desc">'
    'Explore earlier transactions from the previous 24 hours '
    'that share a card, address, email domain, or device with '
    'the selected transaction.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SELECT CONNECTIONS
# ============================================================

if (
    len(graph_connections) > 0
    and
    selected_transaction_id
    in graph_connections.index
):

    selected_connections = (
        graph_connections.loc[
            [selected_transaction_id]
        ].copy()
    )

else:

    selected_connections = pd.DataFrame(
        columns=[
            "Source_Transaction",
            "Related_Transaction",
            "Connection_Type",
            "Actual_Fraud"
        ]
    )


# ============================================================
# CONNECTION ANALYSIS
# ============================================================

if len(selected_connections) > 0:

    total_connections = len(
        selected_connections
    )

    fraud_connections = int(
        selected_connections[
            "Actual_Fraud"
        ].sum()
    )

    nonfraud_connections = (
        total_connections
        - fraud_connections
    )

    fraud_share = (
        fraud_connections /
        total_connections *
        100
    )


    n1, n2, n3, n4 = st.columns(4)


    with n1:
        kpi_card(
            "◎",
            "HISTORICAL CONNECTIONS",
            f"{total_connections:,}"
        )


    with n2:
        kpi_card(
            "●",
            "KNOWN FRAUD-LABELED",
            f"{fraud_connections:,}"
        )


    with n3:
        kpi_card(
            "●",
            "KNOWN NON-FRAUD",
            f"{nonfraud_connections:,}"
        )


    with n4:
        kpi_card(
            "%",
            "FRAUD-LABELED SHARE",
            f"{fraud_share:.2f}%"
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # ========================================================
    # CONNECTION TYPES
    # ========================================================

    connection_types = (
        selected_connections[
            "Connection_Type"
        ]
        .str.split(", ")
        .explode()
        .value_counts()
    )


    st.markdown(
        "#### Shared-Entity Evidence"
    )


    fig_types = go.Figure(
        go.Bar(
            x=connection_types.index,
            y=connection_types.values,

            marker_color=[
                "#8B5CF6",
                "#38BDF8",
                "#34D399",
                "#FBBF24"
            ][:len(connection_types)],

            text=connection_types.values,

            textposition="outside"
        )
    )


    fig_types.update_layout(
        height=350,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,.015)",

        xaxis_title="Shared Entity",
        yaxis_title="Historical Connections",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=25,
            b=20
        )
    )


    st.plotly_chart(
        fig_types,
        use_container_width=True
    )


    # ========================================================
    # GRAPH DISPLAY SUBSET
    # ========================================================

    MAX_GRAPH_NODES = 150


    fraud_neighbors = (
        selected_connections.loc[
            selected_connections[
                "Actual_Fraud"
            ] == 1
        ].copy()
    )


    nonfraud_neighbors = (
        selected_connections.loc[
            selected_connections[
                "Actual_Fraud"
            ] == 0
        ].copy()
    )


    if len(fraud_neighbors) >= MAX_GRAPH_NODES:

        display_connections = (
            fraud_neighbors.sample(
                n=MAX_GRAPH_NODES,
                random_state=42
            )
        )

    else:

        remaining_slots = (
            MAX_GRAPH_NODES
            - len(fraud_neighbors)
        )


        if len(
            nonfraud_neighbors
        ) > remaining_slots:

            sampled_nonfraud = (
                nonfraud_neighbors.sample(
                    n=remaining_slots,
                    random_state=42
                )
            )

        else:

            sampled_nonfraud = (
                nonfraud_neighbors
            )


        display_connections = pd.concat(
            [
                fraud_neighbors,
                sampled_nonfraud
            ],
            ignore_index=True
        )


    displayed_connections = len(
        display_connections
    )


    # ========================================================
    # NETWORK
    # ========================================================

    st.markdown(
        "#### Interactive Relationship Map"
    )


    net = Network(
        height="660px",
        width="100%",
        bgcolor="#080C15",
        font_color="#F8FAFC",
        directed=False,
        cdn_resources="in_line"
    )


    net.add_node(
        selected_transaction_id,

        label=(
            f"SELECTED\n"
            f"{selected_transaction_id}"
        ),

        title=(
            f"Selected transaction"
            f"<br>Risk score: {risk_percent:.2f}%"
            f"<br>Model decision: {prediction_text}"
        ),

        color="#8B5CF6",
        size=42,
        borderWidth=4
    )


    for _, row in display_connections.iterrows():

        related_id = int(
            row["Related_Transaction"]
        )

        related_fraud = int(
            row["Actual_Fraud"]
        )

        connection_type = str(
            row["Connection_Type"]
        )


        if related_fraud == 1:

            node_color = "#FB7185"
            node_size = 20

        else:

            node_color = "#34D399"
            node_size = 11


        net.add_node(
            related_id,

            label=str(
                related_id
            ),

            title=(
                f"Transaction: {related_id}"
                f"<br>Known fraud label: {related_fraud}"
                f"<br>Shared entity: {connection_type}"
            ),

            color=node_color,
            size=node_size
        )


        net.add_edge(
            selected_transaction_id,
            related_id,

            title=(
                f"Shared: {connection_type}"
            ),

            color="#334155"
        )


    net.set_options("""
    {
      "nodes": {
        "shape": "dot",
        "font": {
          "size": 10,
          "color": "#E2E8F0"
        },
        "borderWidth": 1
      },

      "edges": {
        "width": 0.8,
        "color": {
          "color": "#334155",
          "highlight": "#A78BFA"
        },
        "smooth": {
          "type": "continuous"
        }
      },

      "interaction": {
        "hover": true,
        "tooltipDelay": 70,
        "navigationButtons": true,
        "keyboard": true
      },

      "physics": {
        "enabled": true,

        "barnesHut": {
          "gravitationalConstant": -7000,
          "centralGravity": 0.13,
          "springLength": 110,
          "springConstant": 0.025,
          "damping": 0.42
        },

        "stabilization": {
          "iterations": 200
        }
      }
    }
    """)


    graph_html_path = os.path.join(
        BASE_DIR,
        "makamin_network_temp.html"
    )


    net.save_graph(
        graph_html_path
    )


    with open(
        graph_html_path,
        "r",
        encoding="utf-8"
    ) as file:

        graph_html = file.read()


    components.html(
        graph_html,
        height=660,
        scrolling=False
    )


    # ========================================================
    # LEGEND
    # ========================================================

    l1, l2, l3 = st.columns(3)


    with l1:
        st.markdown(
            '<div class="legend-box">'
            '🟣 <b>Selected Transaction</b>'
            '</div>',
            unsafe_allow_html=True
        )


    with l2:
        st.markdown(
            '<div class="legend-box">'
            '🔴 <b>Known Fraud-Labeled</b>'
            '</div>',
            unsafe_allow_html=True
        )


    with l3:
        st.markdown(
            '<div class="legend-box">'
            '🟢 <b>Known Non-Fraud</b>'
            '</div>',
            unsafe_allow_html=True
        )


    st.markdown(
        f"""
<div class="explain-card">
<b>Relationship context</b><br><br>
The selected transaction has
<b>{total_connections:,}</b> historical connections in its
complete previous-24-hour neighborhood, including
<b>{fraud_connections:,}</b> connections to transactions
with known fraud labels.
<br><br>
For readability, the interactive map displays
<b>{displayed_connections:,}</b> connections. Fraud-labeled
neighbors are retained first when the neighborhood exceeds
the display limit, while dashboard statistics continue to use
the complete neighborhood.
<br><br>
Shared entities are investigative signals only and do not
independently establish coordinated fraud.
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # EXPANDERS
    # ========================================================

    with st.expander(
        "View displayed relational evidence"
    ):

        st.dataframe(
            display_connections[
                [
                    "Related_Transaction",
                    "Connection_Type",
                    "Actual_Fraud"
                ]
            ],

            use_container_width=True,
            hide_index=True
        )


    with st.expander(
        "View complete neighborhood summary"
    ):

        summary_data = pd.DataFrame({

            "Metric": [
                "Historical connections",
                "Known fraud-labeled connections",
                "Known non-fraud connections",
                "Fraud-labeled share",
                "Connections displayed"
            ],

            "Value": [
                f"{total_connections:,}",
                f"{fraud_connections:,}",
                f"{nonfraud_connections:,}",
                f"{fraud_share:.2f}%",
                f"{displayed_connections:,}"
            ]
        })


        st.dataframe(
            summary_data,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# NO CONNECTIONS
# ============================================================

else:

    st.markdown(
        """
<div class="explain-card">
<b>No historical relational evidence found.</b>
<br><br>
No earlier transaction in the previous 24 hours shared the
investigated card, address, email domain, or device.
The absence of a historical neighborhood does not determine
whether the selected transaction is fraudulent.
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# CONTEXT / LIMITATIONS
# ============================================================

st.markdown(
    '<div class="soft-divider"></div>',
    unsafe_allow_html=True
)


st.markdown(
    """
<div class="explain-card">
<b>Evaluation context</b><br><br>
Population-level analytics use the complete chronological
validation set of <b>118,108 transactions</b>.
Transaction-level investigation is available for
<b>5,000 validation transactions</b> with local SHAP
explanations.
<br><br>
Known fraud labels are displayed for evaluation and
demonstration only. They would not be available when scoring
a new transaction in deployment. Historical relationships use
only earlier transactions from the previous 24 hours.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer-box">
<div class="footer-brand">MAKĀMIN | مكامن</div>
<div class="footer-tagline">Uncovering Hidden Fraud Patterns</div>
<br>
Fraud Analytics &amp; Investigation Workspace
<br>
Enhanced XGBoost &nbsp;•&nbsp;
Explainable AI (SHAP) &nbsp;•&nbsp;
Historical Relational Analysis
</div>
""",
    unsafe_allow_html=True
)

