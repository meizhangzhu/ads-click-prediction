import matplotlib.pyplot as plt

#Extract features and save as SVM light format
fin = open('data_train.csv')

featname = fin.readline().strip().split(',')

#Load the maximum index
maxID = {}
finID = open('maxID.txt')

for line in finID:
    i,id = line.strip().split('\t')
    maxID[featname[int(i)]] = int(id) + 1

fout = open('train_svm.txt','w')

# feat_to_add = [1, 2, 3] # 49.6783%
feat_to_add = [1, 2, 3, 4, 5, 7, 8, 10] # 81.0425%
# feat_to_add = [1, 2, 3, 4, 5, 7, 8, 9, 10, 13] # 80.9907%


#Use advertiser_id,campaign_id,category_id
X = []
user_id_dict = {}
p_count = 0
n_count = 0
for line in fin:
    data = line.strip().split(',')

    # user_id = data[6]
    # if user_id in user_id_dict:
    #     user_id_dict[user_id] += 1
    # else:
    #     user_id_dict[user_id] = 1

    if data[14] == '0':
        n_count += 1
        click = '-1'
        # click = "0"
    else:
        p_count += 1
        click = '+1'
    #In SVM format, index start with 1 while it starts with 0 in python
#     x = []
#     current_vec_len = 0
#     for feat_id in feat_to_add:
#         x.append(str(int(data[feat_id])+1+current_vec_len))
#         current_vec_len += maxID[featname[feat_id]]
#
#     x_svm = [click]
#     for index in x:
#         x_svm.append(index + ':1')
#
#     if data[11] == '':
#         data[11] = '0'
#     if data[12] == '':
#         data[12] = '0'
#     x_svm.append(str(current_vec_len + 1) + ':' + str(1.0*int(data[11])/int(maxID[featname[11]])))
#     x_svm.append(str(current_vec_len + 2) + ':' + str(1.0*int(data[12])/int(maxID[featname[12]])))
#
#     X.append(x_svm)
#
#
# for x in X:
#     fout.write(' '.join(x) + '\n')

fin.close()
fout.close()

# with open("train_small.dat", "w+") as fout:
#     for x in X[:int(0.8*len(X))]:
#         fout.write(' '.join(x) + '\n')
#
# with open("valid.dat", "w+") as fout:
#     for x in X[int(0.8*len(X)):]:
#         fout.write(' '.join(x) + '\n')
#
# #Extract features and save as SVM light format
# fin = open('data_test.csv')
# fin.readline()
#
# fout = open('test_svm.txt','w')
#
# for line in fin:
#     data = line.strip().split(',')
#
#     #In SVM format, index start with 1 while it starts with 0 in python
#     x = []
#     current_vec_len = 0
#     for feat_id in feat_to_add:
#         x.append(str(int(data[feat_id])+1+current_vec_len))
#         current_vec_len += maxID[featname[feat_id]]
#
#     x_svm = ['0']
#     for index in x:
#         x_svm.append(index + ':1')
#
#     if data[11] == '':
#         data[11] = '0'
#     if data[12] == '':
#         data[12] = '0'
#     x_svm.append(str(current_vec_len + 1) + ':' + str(1.0*int(data[11])/int(maxID[featname[11]])))
#     x_svm.append(str(current_vec_len + 2) + ':' + str(1.0*int(data[12])/int(maxID[featname[12]])))
#
#     fout.write(' '.join(x_svm) + '\n')
#
#
# fin.close()
# fout.close()

data_fig = [n_count, p_count]
labels = ['Not click', 'click']

plt.bar(range(len(data_fig)), data_fig, color='rgb', tick_label = labels) # or `color=['r', 'g', 'b']`
plt.show()
