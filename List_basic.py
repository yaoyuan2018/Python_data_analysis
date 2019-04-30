# 使用方括号创建一个列表
# 用len()计算列表中的数量
# 用max()和min()找出最大值和最小值
# 用count()计算出列表中某个值出现的次数
a_list = [1, 2, 3]
print("Output #58:{}".format(a_list))
print("Output #59:a_list has {} elements.".format(len(a_list)))
print("Output #60:the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61:the minimum value in a_list is {}.".format(min(a_list)))


another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))

print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

print("Output #73: {}",format(a_list[0:2]))
print("Output #74: {}",format(another_list[:2]))
print("Output #73: {}",format(a_list[1:3]))
print("Output #73: {}",format(another_list[1:]))

# 使用[:]复制一个列表
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

# 使用+将两个或更多个列表连接起来
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))

# 使用in和not in来检查列表中是否有特定元素
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
  print("Output #80: 2 is in {}".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
  print("Output #82: 6 is not in {}.".format(a_list))


# 使用append()向列表末尾追加一个新元素
# 使用remove()从列表中删除一个特定元素
# 使用pop()从列表末尾删除一个元素
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# 使用reverse()原地反转一个列表会修改原列表
# 要想反转列表同时又不修改原列表，可以先复制列表
a_list.reverse()
print("Output #86: {}".format(a_list))

a_list.reverse()
print("Output #87: {}".format(a_list))


# 使用sort()对列表进行原地排序会修改原列表
# 要想对列表进行排序同时又不修改元列表，可以先复制列表
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))

list_copy = unordered_list[:]
list_copy.sort()

print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# 使用sorted()对一个列表集合按照列表中某个位置的元素进行排序
my_lists = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 1, 3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key = lambda index_value:\
index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

from operator import itemgetter
# 使用itemgetter()对一个列表集合按照两个索引位置来排序
my_lists = [[123, 2, 2, 444], [22, 6, 6, 444], [354, 4, 4, 678], [236, 5, 5, 678],\
[578, 1, 1, 290], [461, 1, 1, 290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3, 0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))