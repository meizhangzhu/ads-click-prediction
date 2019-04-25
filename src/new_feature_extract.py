import json
import pandas

id_feat_names = ["advertiser_id", "campaign_id", "category_id", "adnw_id", "adspot_id", "user_type_id", "media_id", "is_app", "game_feed_id"]
max_ids = []

with open("id_mapping.json") as f:
    id_mapping_dict = json.load(f)

# id feature one-hot vector length
for id_feat_name in id_feat_names:
    max_ids.append(len(id_mapping_dict[id_feat_name])+1)
# hour feature one-hot vector length
max_ids.append(24)

def x_from_row(row):
    x = []
    # id features
    for id_feat_name in id_feat_names:
        original_feat_id = row[id_feat_name]
        feat_id_mapping_dict = id_mapping_dict[id_feat_name]
        val = feat_id_mapping_dict[str(original_feat_id)]
        x.append(val)
    datetime = pandas.to_datetime(row["logged_at"])
    # hour feature
    hour = datetime.hour
    x.append(hour)
    return x

print("reading training data")
X_trn = []
X_tst = []
Y_trn = []
Y_tst = []
df = pandas.read_csv("data_train.csv", index_col=False)
for index, row in df.iterrows():
    x = x_from_row(row)
    y = 1 if int(row["click"]) == 1 else -1
    X_trn.append(x)
    Y_trn.append(y)

print("reading test data")
df = pandas.read_csv("data_test.csv", index_col=False)
for index, row in df.iterrows():
    x = x_from_row(row)
    y = 0
    X_tst.append(x)
    Y_tst.append(y)

dataset = {"X_trn": X_trn, "X_tst": X_tst, "Y_trn": Y_trn, "Y_tst": Y_tst}
with open("dataset.dat", "w+") as f:
    json.dump(dataset, f)

def x_and_y_to_line(x, y):
    elements = []
    # y
    elements.append(str(y))
    # x
    vec_idx = 1
    for feat_idx, val in enumerate(x):
        elements.append("{}:{}".format(vec_idx+val, 1))
        vec_idx += max_ids[feat_idx]
    # x, y to line
    line = " ".join(elements)
    return line

print("writing train data")
with open("trn.dat", "w+") as f:
    for x, y in zip(X_trn, Y_trn):
        line = x_and_y_to_line(x, y)
        f.write(line+"\n")

print("writing test data")
with open("tst.dat", "w+") as f:
    for x, y in zip(X_tst, Y_tst):
        line = x_and_y_to_line(x, y)
        f.write(line+"\n")

print("writing validation data")
len_trn = len(X_trn)
X_valid_trn = X_trn[:int(0.8*len_trn)]
X_valid_tst = X_trn[int(0.8*len_trn):]
Y_valid_trn = Y_trn[:int(0.8*len_trn)]
Y_valid_tst = Y_trn[int(0.8*len_trn):]
with open("valid_trn.dat", "w+") as f:
    for x, y in zip(X_valid_trn, Y_valid_trn):
        line = x_and_y_to_line(x, y)
        f.write(line+"\n")
with open("valid_tst.dat", "w+") as f:
    for x, y in zip(X_valid_tst, Y_valid_tst):
        line = x_and_y_to_line(x, y)
        f.write(line+"\n")
