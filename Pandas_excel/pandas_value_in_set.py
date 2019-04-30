import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'value_in_set.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
important_dates = ['01/24/2013', '01/31/2013']

# pandas提供了isin函数
data_frame_value_in_set = data_frame[data_frame['PurchaseDate']\
    .isin(important_dates)]
writer = pd.ExcelWriter(output_file)

data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_poutput', index=False)
writer.save()