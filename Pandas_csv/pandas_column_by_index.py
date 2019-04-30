import pandas as pd
input_file = "supplier_data.csv"
output_file = "column_by_index.csv"

data_frame = pd.read_csv(input_file)

# 使用iloc函数来根据索引位置选取第1列和第4列
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(output_file, index=False)