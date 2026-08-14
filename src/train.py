import joblib
import pandas as pd


from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier


from sklearn.metrics import (
    roc_auc_score
)


from src.data_loader import load_data
from src.feature_engineering import create_features
from src.threshold_optimizer import find_best_threshold



print("=" * 50)
print("Loading data...")


df = load_data()


print("Original shape:")
print(df.shape)



# ==================================================
# Feature Engineering
# ==================================================

print("=" * 50)
print("Feature Engineering...")


df = create_features(df)


print("Feature shape:")
print(df.shape)



# ==================================================
# Split X / y
# ==================================================

X = df.drop(
    "SeriousDlqin2yrs",
    axis=1
)


y = df[
    "SeriousDlqin2yrs"
]



X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)



print("=" * 50)
print("Training models...")



models = {}



# ==================================================
# Logistic Regression baseline
# ==================================================

lr = LogisticRegression(

    max_iter=3000,

    class_weight="balanced",

    solver="liblinear"

)


lr.fit(
    X_train,
    y_train
)


models["LR"] = lr




# ==================================================
# Random Forest
# ==================================================

rf = RandomForestClassifier(

    n_estimators=300,

    max_depth=8,

    class_weight="balanced",

    random_state=42,

    n_jobs=-1

)


rf.fit(
    X_train,
    y_train
)


models["RF"] = rf




# ==================================================
# XGBoost
# ==================================================

xgb = XGBClassifier(

    n_estimators=300,

    max_depth=5,

    learning_rate=0.05,

    scale_pos_weight=10,

    random_state=42,

    eval_metric="logloss"

)


xgb.fit(
    X_train,
    y_train
)


models["XGB"] = xgb




# ==================================================
# Threshold Optimization
# ==================================================

print("=" * 50)
print("Threshold Optimization")



model_results = {}



for name, model in models.items():


    print("\nModel:", name)



    probabilities = model.predict_proba(
        X_test
    )[:, 1]



    auc = roc_auc_score(
        y_test,
        probabilities
    )



    best_threshold, threshold_table = find_best_threshold(

        y_test,

        probabilities

    )



    model_results[name] = {


        "AUC":
            auc,


        "best_threshold":
            best_threshold["threshold"],


        "precision":
            best_threshold["precision"],


        "recall":
            best_threshold["recall"],


        "F1":
            best_threshold["f1"]

    }



    print(
        "AUC:",
        round(auc,4)
    )


    print(
        "Best Threshold:",
        best_threshold["threshold"]
    )


    print(
        "Precision:",
        round(best_threshold["precision"],4)
    )


    print(
        "Recall:",
        round(best_threshold["recall"],4)
    )


    print(
        "F1:",
        round(best_threshold["f1"],4)
    )





# ==================================================
# Model Comparison
# ==================================================

print("=" * 50)
print("Model Comparison")



result_df = pd.DataFrame(
    model_results
).T



print(result_df)



result_df.to_csv(
    "models/model_results.csv"
)



# ==================================================
# Select Best Model
# ==================================================

best_model_name = (

    result_df["F1"]
    .idxmax()

)



best_model = models[
    best_model_name
]



best_threshold = (

    result_df
    .loc[
        best_model_name,
        "best_threshold"
    ]

)



print("=" * 50)

print(
    "Best Model:",
    best_model_name
)


print(
    "Best Threshold:",
    best_threshold
)



# ==================================================
# Save
# ==================================================


joblib.dump(

    best_model,

    "models/best_model.pkl"

)



joblib.dump(

    best_threshold,

    "models/best_threshold.pkl"

)



joblib.dump(

    models["LR"],

    "models/lr_model.pkl"

)



joblib.dump(

    models["RF"],

    "models/rf_model.pkl"

)



joblib.dump(

    models["XGB"],

    "models/xgb_model.pkl"

)



joblib.dump(

    X.columns.tolist(),

    "models/features.pkl"

)



print("=" * 50)

print(
    "Training finished."
)