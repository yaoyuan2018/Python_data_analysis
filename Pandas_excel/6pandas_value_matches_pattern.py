import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = '6_value_matches_pattern.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_matches_pattern = data_frame[data_frame['Customer Name']\
    .str.startswith("J")]
writer = pd.ExcelWriter(output_file)

data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output',\
                                          index=False)
writer.save()