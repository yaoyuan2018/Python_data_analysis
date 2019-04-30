import pandas as pd
input_file = 'supplier_data.csv'
output_file = 'column_by_name.csv'

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)