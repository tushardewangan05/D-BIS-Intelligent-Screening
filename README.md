# D-BIS – Intelligent Screening

## AI-Driven Anomaly Detection in Component Burn-In & Screening

D-BIS (Data-Based Intelligent Screening) is a Python-based intelligent screening solution designed to detect abnormal behavior, parameter drift, and potential reliability issues in electronic components during Burn-In and Environmental Stress Screening (ESS).

The system analyzes component test data, performs data preprocessing and statistical analysis, generates anomaly scores, monitors parameter trends, analyzes drift, and presents the results through an interactive dashboard for reliability-focused decision making.

---

## 🚀 Live Prototype

**Live D-BIS Prototype:**

https://tushardewangan05.github.io/D-BIS-Intelligent-Screening/

---

**Problem Statement:** AI-Driven Anomaly Detection in Component Burn-In & Screening

**Domain:** Electronic Component Reliability, Artificial Intelligence & Data Analytics

---

# 📌 Problem Statement

High-reliability electronic components undergo Burn-In and Environmental Stress Screening (ESS) to identify defective or potentially unreliable components before they are deployed in critical systems.

Traditional screening methods mainly rely on fixed threshold-based PASS/FAIL limits.

However, a component can remain within the acceptable limits while showing:

- Gradual parameter drift
- Abnormal trends
- Early degradation
- Latent defects
- Unusual behavior compared with normal components
- Potential future reliability issues

Static threshold-based screening may therefore miss subtle changes in component behavior.

D-BIS addresses this challenge by using data-driven analysis, anomaly detection, trend monitoring, and time-series drift analysis.

---

# 💡 Proposed Solution

D-BIS converts raw component test data into meaningful reliability insights.

The solution analyzes component parameters across different stages of Burn-In and Screening and identifies components that show abnormal behavior.

Instead of depending only on a fixed PASS/FAIL threshold, D-BIS considers:

- Parameter behavior
- Statistical variation
- Anomaly score
- Component-to-component comparison
- Parameter trends
- Drift behavior
- Future-value estimation
- Screening status

---

# 🎯 Main Objectives

The main objectives of D-BIS are:

1. Detect abnormal component behavior.
2. Identify statistical outliers.
3. Generate an anomaly score for each component.
4. Monitor parameter behavior during Burn-In.
5. Detect gradual parameter drift.
6. Analyze early-stage values to estimate later behavior.
7. Classify components into different screening categories.
8. Provide an interactive visualization dashboard.
9. Improve explainability of screening decisions.
10. Support reliability-focused component analysis.

---

# 🧩 Core Modules

## Module A – Dynamic Outlier Detection

Module A focuses on detecting abnormal component behavior from Burn-In and Screening test data.

### Key Functions

- Component test data analysis
- Parameter-wise analysis
- Data preprocessing
- Statistical analysis
- Outlier detection
- Anomaly score generation
- Component comparison
- Abnormal component identification
- Screening classification
- Reliability-focused analysis

### Module A Process

Component Test Data
        ↓
Data Preprocessing
        ↓
Parameter Analysis
        ↓
Statistical Analysis
        ↓
Outlier Detection
        ↓
Anomaly Score
        ↓
Screening Classification

---

## Module B – Time-Series Drift Predictor

Module B focuses on monitoring parameter behavior over different stages of component testing.

The system can analyze measurements such as:

Value_0h
   ↓
Value_24h
   ↓
Value_168h

The early measurements can be analyzed to understand the trend and estimate future behavior.

### Key Functions

- Time-series analysis
- Parameter trend monitoring
- Drift analysis
- Drift slope calculation
- Future-value estimation
- Component-wise comparison
- Trend visualization
- Potential degradation identification

### Module B Process

Value_0h + Value_24h
        ↓
Trend Analysis
        ↓
Drift Calculation
        ↓
Future Value Estimation
        ↓
Value_168h Analysis
        ↓
Safety / Drift Evaluation

---

# 🔄 Complete D-BIS Process Flow

The complete system workflow is:

Component Test Data
        ↓
CSV Data Input
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Feature Preparation
        ↓
Parameter Analysis
        ↓
Anomaly Detection
        ↓
Anomaly Score Generation
        ↓
Time-Series / Drift Analysis
        ↓
Future Behavior Analysis
        ↓
Screening Classification
        ↓
Interactive Dashboard
        ↓
Reliability Insights

---

# 🏗️ System Architecture

```text
                  ┌─────────────────────────┐
                  │  Component Test Data    │
                  │      / CSV File         │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │    Data Preprocessing   │
                  │ Cleaning & Preparation  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Parameter & Feature     │
                  │       Analysis          │
                  └────────────┬────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
      ┌─────────────────────┐      ┌─────────────────────┐
      │      Module A       │      │      Module B       │
      │ Anomaly Detection   │      │ Drift Prediction    │
      └──────────┬──────────┘      └──────────┬──────────┘
                 │                            │
                 ▼                            ▼
      ┌─────────────────────┐      ┌─────────────────────┐
      │   Anomaly Score     │      │ Trend / Drift Score │
      └──────────┬──────────┘      └──────────┬──────────┘
                 │                            │
                 └──────────────┬─────────────┘
                                ▼
                     ┌─────────────────────┐
                     │ Screening Decision  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Interactive         │
                     │ Dashboard           │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Reliability         │
                     │ Insights            │
                     └─────────────────────┘
