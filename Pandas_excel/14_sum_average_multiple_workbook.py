import glob
import pandas as pd
import os

input_file = 'Excel_result/sales_2013.xlsx'
output_file = 'Excel_result/14_output.xls'

all_workbooks = glob.glob(os.path.join(input_file, '*.xls*'))
data_frame = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheetname = None, index_col=None)
    workbook_total_sales = []
    workbook_number_of_sales = []
    worksheet_data_frames = []
    worksheet_data_frame = None
    workbook_data_frame = None
    for worksheet_name, data in all_worksheets.items():
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(\
            ',',''))for value in data.loc[:, 'Sale Amount']]).sum()
        number_of_sales = len(data.loc[:, 'Sale Amount'])
        average_sales = pd.DataFrame(total_sales / number_of_sales)


