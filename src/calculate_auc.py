import numpy as np
from sklearn.metrics import roc_auc_score

ground_truth_fn = "valid_tst_converted.dat"
pred_fn = "valid_output"

y_true = []
y_pred = []
with open(ground_truth_fn) as f:
    for line in f.readlines():
        if line.strip() == "":
            break
        y = line.split(" ")[0]
        y_true.append(int(y))

# with open(pred_fn) as f:
#     for line in f.readlines():
#         if line.strip() == "":
#             break
#         y = line.strip()
#         y_pred.append(float(y))

with open(pred_fn) as f:
    for line in f.readlines()[1:]:
        if line.strip() == "":
            break
        y = line.strip().split(" ")[1]
        y_pred.append(float(y))

y_true = np.array(y_true)
y_pred = np.array(y_pred)
score = roc_auc_score(y_true, y_pred)
print(score)
