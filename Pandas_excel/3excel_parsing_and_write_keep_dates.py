from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
# 从datetime模块导入date函数，我们可以将数值转换成日期并对日期进行格式化
# xldate_as_tuple可以将Excel中代表日期、时间或日期时间的数值转换为元组。
# 只要将数值转换成了元组，就可以提取出具体时间元素（例如：年、月、日）并将时间元素格式化成不同的时间格式

input_file = 'sales_2013.xlsx'
output_file = '3_result.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):

            # 检验单元格类型是否为数字3。单元格类型为3表示这个单元格中包含日期数据。
            if worksheet.cell_type(row_index, col_index) == 3:
                # 使用worksheet对象的cell_value函数和行列索引来引用单元格中的值。
                # 这个单元格中的值作为xldate_as_tuple函数中的第一个参数，会被转换成元组中的一个代表日期的浮点数。
                date_cell = xldate_as_tuple(worksheet.cell_value \
                                                (row_index, col_index), workbook.datemode)  # 参数workbook.datemode是必需的，它可以使函数确定日期是基于1900年还是基于1904年

                # 使用元组索引来引用元组date_cell中的前3个元素（年、月、日）并将他们作为参数传给date函数
                # strftime函数将date对象转换为一个具有特定格式的字符串。格式'%m/%d/%Y'表示像2019年4月26日这样的日期应该显示为04/26/2019
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)

            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)

output_workbook.save(output_file)
