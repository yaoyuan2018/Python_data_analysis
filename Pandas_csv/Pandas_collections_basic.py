import pandas as pd

input_file = "../supplier_data.csv"
output_file = "supplier_data_output.csv"
data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].\
    isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index = False)
