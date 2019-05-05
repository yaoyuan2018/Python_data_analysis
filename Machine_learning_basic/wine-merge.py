import csv
import pandas as pd
import numpy as np

input_file = 'winequality-white.csv'
output_file = 'wine_white_test.csv'
data = []

data_frame = pd.read_csv(input_file,header=None)
for index,row in data_frame.iterrows():
    data.append(row[0].split(';'))
save_model = pd.DataFrame(data)

print(data[0])
save_model.to_csv(output_file,index_label=0,header=None,index=None)



# data = np.array(data_frame.loc[:,:])
# print(data)

# column1 = data_frame.iloc[:,[0]]
# print(column1)

# for row in column1:
#     print(row[0])

# for indexs in data_frame.index:
#     print(data_frame.iloc[indexs].values[0:-1])
# data_frame.set_index(data)
# print(data_frame)

# for index, row in data_frame.iterrows():
#     print(row[0].split(';'))