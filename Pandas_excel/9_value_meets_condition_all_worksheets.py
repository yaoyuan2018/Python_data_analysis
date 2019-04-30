import pandas as pd

input_file = 'Excel_result/sales_2013.xlsx'
output_file = 'Excel_result/9.xls'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])

# axis = 0代表跨行（down），而 axis = 1代表跨列（across）
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000',index=False)
writer.save()