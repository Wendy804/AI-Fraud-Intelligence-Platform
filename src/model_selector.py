import pandas as pd
import joblib



def select_best_model(
        result_path="models/model_results.csv"
):


    df = pd.read_csv(
        result_path,
        index_col=0
    )


    # 按F1选择
    best_model = (
        df["F1"]
        .idxmax()
    )


    best_threshold = (
        df.loc[
            best_model,
            "best_threshold"
        ]
    )


    print("="*50)

    print(
        "Best Model:",
        best_model
    )

    print(
        "Best Threshold:",
        best_threshold
    )

    print("="*50)



    # 模型路径

    model_map = {

        "LR":
        "models/lr_model.pkl",

        "RF":
        "models/rf_model.pkl",

        "XGB":
        "models/xgb_model.pkl"

    }


    model = joblib.load(
        model_map[best_model]
    )


    # 保存最终模型


    joblib.dump(
        model,
        "models/best_model.pkl"
    )


    joblib.dump(
        best_threshold,
        "models/best_threshold.pkl"
    )


    return (
        best_model,
        best_threshold
    )



if __name__ == "__main__":

    select_best_model()