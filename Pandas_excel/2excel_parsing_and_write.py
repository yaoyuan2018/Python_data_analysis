from xlrd import open_workbook
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = '2_result.xls'

# 实例化一个xlwt Workbook对象，以使我们可以将结果写入用于输出的Excel文件
output_workbook = Workbook()

# 使用xlwt的add_sheet函数为输出工作簿添加一个工作表jan_2013_output
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 使用xlrd的open_workbook函数打开用于输入的工作簿，并将结果赋给一个workbook对象
with open_workbook(input_file) as workbook:

    # 使用workbook对象的sheet_by_nmae函数引用名称为january_2013的工作表
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, \
                                   worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)