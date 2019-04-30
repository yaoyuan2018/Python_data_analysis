import csv
import pandas as pd

input_file = 'winequality-red.csv'
output_file = 'test.csv'

data_frame = pd.read_csv(input_file,index_col=None)

# column1 = data_frame.iloc[:,[0]]

# for row in column1:
#     print(row[0])问卷选择题样式

# for indexs in data_frame.index:
#     print(data_frame.iloc[indexs].values[0:-1])
# data_frame.set_index(data)
# print(data_frame)

for index, row in data_frame.iterrows():
    print(row[0].split(';'))