import pandas as pd
input_file = 'supplier_data.csv'
output_file = 'select_contiguous_rows.csv'

data_frame = pd.read_csv(input_file, header=None)

#丢弃前3行和最后3行（索引为0,1,2和16,17,18的那些行）
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
data_frame.columns = data_frame.iloc[0]
#
print(data_frame)
print(data_frame.drop(3))

# #reindex函数为数据框重新生成索引
# data_frame = data_frame.reindex(data_frame.drop(3))
# data_frame.to_csv(output_file, index=False)