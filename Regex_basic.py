import re
# # 计算字符串中模式出现的次数
# string = "The quick brown fox jumps over the lazy dog."
# string_list = string.split()
# pattern = re.compile(r"The", re.I)
# count = 0
#
# for word in string_list:
#     if pattern.search(word):
#         count += 1
# print("Output #38: {0:d}".format(count))

# 在字符串中每次找到模式时将其打印出来
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>)The", re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

# 使用字母“a”替换字符串中的单词“the”
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"

# 将正则表达式赋给变量pattern
pattern = re.compile(string_to_find, re.I)

# 使用re.sub函数以不区分大小写的方式在变量string中寻找模式，然后将每个模式替换成字母a。
print("Output #40: {:s}".format(pattern.sub("a", string)))