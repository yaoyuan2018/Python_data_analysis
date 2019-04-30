import pandas as pd

input_file = "supplier_data.csv"
output_file = "regex_test.csv"
data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].\
    str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index = False)