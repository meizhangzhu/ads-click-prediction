import json
import pandas

feat_names = ["advertiser_id", "campaign_id", "category_id", "adnw_id", "adspot_id", "uid", "user_type_id", "media_id", "is_app", "game_feed_id"]

feat_dict = {}
for feat_name in feat_names:
    feat_dict[feat_name] = {}

df = pandas.read_csv("data_train.csv", index_col=False)
for index, row in df.iterrows():
    for feat_name in feat_names:
        feat_value = row[feat_name]
        if feat_value not in feat_dict[feat_name]:
            feat_dict[feat_name][feat_value] = len(feat_dict[feat_name])

df = pandas.read_csv("data_test.csv", index_col=False)
for index, row in df.iterrows():
    for feat_name in feat_names:
        feat_value = row[feat_name]
        if feat_value not in feat_dict[feat_name]:
            feat_dict[feat_name][feat_value] = len(feat_dict[feat_name])

with open("id_mapping.json", "w+") as f:
    json.dump(feat_dict, f)
