# # 有很多标准模块、内置函数和操作符可以用来管理字符串。常用的操作符和函数包括"+"、"*"和"len"。
#
# string1 = "This is a "
# string2 = "short string."
# sentence = string1 + string2
#
# print("Output #18: {0:s}".format(sentence))
#
# # 使用 * 操作符将字符串重复一定的次数
# print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
# m = len(sentence)
# print("Output #20: {0:d}".format(m))
#
# string3 = "Your,deliverable,is,due,in,June"
# string3_list = string3.split(',')
# print("Output #24: {0} {1} {2}".format(string3_list[1], string3_list[5],\
#                                        string3_list[-1]))

string3 = " Remove unwanted characters from this string.\t\t   \n"
print("Output #26: string3: {0:s}".format(string3))

string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))

string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))

string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))

string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")

print("Output #32 (with !@!): {0:s}".format(string5_replace))

string5_replace = string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))

string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))

string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))

string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))

string5_list = string5.split()
print("Output #37 (on each word):")
for word in string5_list:
  print("{0:s}".format(word.capitalize()))