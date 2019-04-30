import glob
import sys
import os

# argv--列表变量。这个变量捕获了传递给Python脚本的命令行参数列表
# 即你在命令行中的所有输入，包括你的脚本名称。
# argv[0]就是脚本名称，argv[1]是命令行中传递给脚本的第一个附加参数
input_file = sys.argv[1]

print("Output #143: ")
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()
"""
sys.argv列表捕获了要读取的文件的路径名，并将路径名赋给变量input_file。
创建了一个文件对象filereader，其中包含了以r模式（只读模式）打开的input_file文件中的各个行。
"""

# 读取多个文本文件
print("Output #145:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))