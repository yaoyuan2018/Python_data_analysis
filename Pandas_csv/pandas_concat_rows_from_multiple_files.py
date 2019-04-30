import pandas as pd
import glob

input_files = glob.glob('sales_*')
output_file = 'csv_merge.csv'
all_data_frames = []
for file in input_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)

data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)