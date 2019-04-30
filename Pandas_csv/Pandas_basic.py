import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_output.csv"
important_dates = ['1/20/14', '1/30/14']

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

# loc函数可以同时选择特定的行与列。
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
    .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)