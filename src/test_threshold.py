import numpy as np

from src.threshold_optimizer import find_best_threshold



y_true = np.array(
    [0,0,0,1,1,1,1,0,1,0]
)


y_prob = np.array(
    [
        0.1,
        0.2,
        0.3,
        0.6,
        0.7,
        0.8,
        0.9,
        0.4,
        0.65,
        0.2
    ]
)



best, all_results = find_best_threshold(
    y_true,
    y_prob
)



print("Best:")
print(best)



print("\nAll:")
for r in all_results:
    print(r)