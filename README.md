# D-BIS – Intelligent Screening

## AI-Driven Anomaly Detection in Component Burn-In & Screening

D-BIS (Data-Based Intelligent Screening) is a Python-based intelligent screening and anomaly detection solution designed for analyzing electronic component test data during **Burn-In and Environmental Stress Screening (ESS)**.

The system analyzes component test parameters, identifies abnormal behavior, generates anomaly scores, performs trend and drift analysis, and presents the results through an interactive dashboard.

---

## 🚀 Live Prototype

🌐 **Live Prototype:**

https://tushardewangan05.github.io/D-BIS-Intelligent-Screening/

---

## 📌 Problem Statement

### AI-Driven Anomaly Detection in Component Burn-In & Screening

High-reliability electronic components are subjected to burn-in and screening tests to identify defective or potentially unreliable components before deployment.

Traditional screening approaches mainly depend on fixed threshold-based PASS/FAIL limits. Such static limits may not always identify components that remain within acceptable limits but show:

- Gradual parameter drift
- Abnormal trends
- Early degradation
- Latent defects
- Unusual behavior compared with the normal component population

D-BIS aims to address this limitation through data-driven analysis, anomaly detection, trend monitoring, and predictive analysis.

---

# 💡 Proposed Solution

D-BIS converts raw component test data into meaningful reliability insights.

### Overall Workflow

```text
Component Test Data
        ↓
CSV Data Input
        ↓
Data Preprocessing
        ↓
Parameter Analysis
        ↓
Anomaly Detection
        ↓
Anomaly Score
        ↓
Trend / Drift Analysis
        ↓
Screening Classification
        ↓
Interactive Dashboard
        ↓
Reliability Insights

# 🧩 Core Modules
Module A – Dynamic Outlier Detection

Module A focuses on detecting abnormal component behavior from burn-in and screening test data.

Key Functions
Component test data analysis
Parameter-wise analysis
Statistical outlier detection
Anomaly score generation
Component comparison
Identification of abnormal components
Screening classification
Reliability-focused analysis
Screening Classification
Status	Meaning
🟢 NORMAL	Component behavior is within the expected range
🟡 WARNING	Component shows unusual behavior and requires attention
🔴 ANOMALY	Component shows significant abnormal behavior


Module B – Time-Series Drift Analysis

Module B focuses on monitoring parameter behavior over different stages of component testing.

The system can analyze values such as:

Value_0h
   ↓
Value_24h
   ↓
Value_168h

The change in parameter values can be analyzed to identify abnormal drift.

Key Functions
Time-series analysis
Parameter trend monitoring
Drift detection
Trend visualization
Component-wise comparison
Future-value analysis
Identification of potentially degrading components
