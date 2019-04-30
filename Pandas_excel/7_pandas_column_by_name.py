import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = '8_column_by_name.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_column_by_name = data_frame.loc[:,['Customer ID', 'Purchase Date']]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_13_output',\
                                   index=False)
writer.save()