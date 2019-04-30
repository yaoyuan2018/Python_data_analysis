# 使用花括号创建字典
# 用冒号分隔键-值对
# 用len()计算出字典中键-值对的数量
empty_dict = {}
a_dict = {'one':1, 'two':2, "three":3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))

another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements"\
.format(len(another_dict)))

# 使用键来引用字典中特定的值
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))

# 使用copy()复制一个字典
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))


# 使用keys()、values()和items()
# 分别引用字典中的键、值和键-值对
print("Output #109: {}".format(a_dict.keys()))

a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}.".format(another_dict.keys()))

if 'c' not in another_dict:
    print("Output #115: c is not a key in another_dict: {}.".format(another_dict.keys()))

print("Output #116: {!s}".format(a_dict.get('three')))

#get函数，如果字典中存在这个键，get函数就返回键值对应的字典值；如果不存在这个键就返回None
#get函数还可以使用第二个参数，表示如果字典中不存在键值时函数的返回值。
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))


# 排序
# 使用sorted()对字典进行排序
# 要想对字典排序的同时不修改原字典
# 先复制字典
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item:item[0])
print("Output #120 (order by keys): {}".format(ordered_dict1))

ordered_dict2 = sorted(dict_copy.items(), key=lambda item:item[1])
print("Output #121 (order by values): {}".format(ordered_dict2))

ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print("Output #122 (order by values, descending): {}".format(ordered_dict3))

ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("Output #123 (order by values, asecending): {}".format(ordered_dict4))