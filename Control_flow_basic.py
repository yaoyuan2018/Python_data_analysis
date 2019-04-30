my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 对于my_data中的每一行，如果这行中索引位置2的值（即第三个值）大于5，则保留这一行。因为6和9都大于5，所以rows_to_keep中的列表子集[4, 5, 6]和[7, 8, 9]。
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}".format(rows_to_keep))


# 使用集合生成式在列表中选择出一组唯一的元组
my_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9)]
set_of_tuples1 = {x for x in my_data}
print("Output #131 (set comprehension): {}".format(set_of_tuples1))

# 使用字典生成式选择特定的键-值对
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print("Output #133 (dictionary comprehension): {}".format(my_results))


print("Output #134:")
x = 0
while x < 11:
  print("{!s}".format(x))
  x+=1

# 计算一系列数值的均值
def getMean(numericValues):
  return sum(numericValues)/len(numericValues)
my_list2 = []

# getMean()中没有检验序列是否包含数值的if语句。
# 简单形式
try:
  print("Output #138: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
  print("Output #138 (Error): {}".format(float('nan')))
  print("Output #138 (Error): {}".format(detail))

# 完整形式
try :
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output #142 (Error): " + str(float('nan')))
    print("Output #142 (Error): ", detail)
else:
    print("Output #142 (The mean is):", result)

finally:
    print("Output #142 (Finally): The finally block is executed every time")