import numpy as np

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)



def find_best_threshold(
    y_true,
    y_prob,
    thresholds=None
):
    """
    Search best classification threshold

    Parameters:
    ----------
    y_true:
        true labels

    y_prob:
        prediction probability

    thresholds:
        list of thresholds


    Returns:
    -------
    best_result
    """



    if thresholds is None:

        thresholds = np.arange(
            0.1,
            0.91,
            0.05
        )



    results = []



    for threshold in thresholds:


        y_pred = (
            y_prob >= threshold
        ).astype(int)



        precision = precision_score(
            y_true,
            y_pred,
            zero_division=0
        )


        recall = recall_score(
            y_true,
            y_pred,
            zero_division=0
        )


        f1 = f1_score(
            y_true,
            y_pred,
            zero_division=0
        )



        results.append({

            "threshold": threshold,

            "precision": precision,

            "recall": recall,

            "f1": f1

        })



    results = sorted(
        results,
        key=lambda x:x["f1"],
        reverse=True
    )



    best_result = results[0]



    return best_result, results
    