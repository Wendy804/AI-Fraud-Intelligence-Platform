AI-Fraud-Intelligence-Platform Overview

AI-Fraud-Intelligence-Platform is an end-to-end AI credit risk assessment platform designed for fraud detection and customer risk analysis.

The platform provides two major applications:

1. Risk Dashboard for business and risk control teams

2. AI Credit Risk Assistant for individual customer assessment

---

 System Architecture

Customer Data

        |

        v

Data Cleaning

        |

        v

Feature Engineering

        |

        v

Machine Learning Risk Model

        |

        +----------------+

        |                |

        v                v

Risk Dashboard     Customer Assistant

        |                |

        v                v

Portfolio Analysis   Individual Assessment

        |

        v

Risk Decision & Report Generation

--- Applications

 1. Risk Dashboard

Location:

dashboard/[app.py](http://app.py)



Purpose:

Designed for business users and risk analysts.

Features:

- CSV customer data upload

- Batch risk prediction

- Risk level classification

- Approval decision

- Customer risk overview

- Model explanation

---

 2. AI Credit Risk Assistant

Location:

customer_portal/[app.py](http://app.py)



Purpose:

Designed for single customer credit assessment.

Features:

- Customer information input

- Automatic feature engineering

- Machine learning prediction

- Risk factor explanation

- Decision recommendation

- PDF risk report generation

---

 Machine Learning Pipeline

Input Data

↓

Feature Engineering

↓

Model Prediction

↓

Risk Threshold Optimization

↓

Risk Classification

↓

Decision Strategy

↓

Explanation Generation

---

 Feature Engineering

The system automatically generates risk-related features:

- Missing value indicators

- Credit utilization

- Payment delay score

- Serious delay flag

- Credit line aggregation

- Income related features

- Debt income ratio

- Age groups

Users do not need to manually calculate derived features.

---

 Models

Implemented models:

- Logistic Regression

- Random Forest

- XGBoost

The production model is selected based on evaluation performance.

---

Technology Stack

Machine Learning

- Python

- Pandas

- Scikit-learn

- XGBoost

 Application

- Streamlit

 Explainability

- Risk factor explanation

- SHAP-ready architecture

 Reporting

- PDF risk assessment report

---

 Project Structure

AI-Fraud-Intelligence-Platform

├── dashboard  
├── customer_portal  
├── src  
├── strategy  
├── models  
├── data  
├── llm_agent  
├── tests  
├── requirements.txt  
└── [README.md](http://README.md)



---

 How to Run

Install dependencies:

```bash

pip install -r requirements.txt

Run Dashboard:

streamlit run dashboard/[app.py](http://app.py)

Run Customer Assistant:

streamlit run customer_portal/[app.py](http://app.py)