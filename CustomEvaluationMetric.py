#Implement a custom metric weighted_accuracy where class 0 has a weight of 1 and class 1 has a weight of 2.

import numpy as np
def weighted_accuracy(y_true, y_pred):
    weights = {0: 1, 1: 2}
    weighted_correct = 0
    weighted_total = 0
    for true, pred in zip(y_true, y_pred):
        weight = weights[true]
        weighted_total += weight
        if true == pred:
            weighted_correct += weight
    return weighted_correct / weighted_total
