from xlrd import open_workbook
# 导入xlrd模块的open_workbook函数来读取和分析Excel文件。
input_file = 'sales_2013.xlsx'

# 使用open_workbook函数打开一个Excel输入文件，并赋给一个名为workbook的对象。
workbook = open_workbook(input_file)

# 打印出工作簿中工作表的数量
print('Number of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets():
    # 打印每个工作表的名称、行与列的数量
    print("Worksheet name:", worksheet.name, '\tRows:',\
          worksheet.nrows, "\tColumns:", worksheet.ncols)

