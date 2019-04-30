import sqlite3

# 创建SQLite3内存数据库
# 创建带有4个属性的sales表

con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
                (customer VARCHAR(20),
                product VARCHAR(40),
                amount FLOAT,
                date DATE);"""
con.execute(query)
con.commit()

# 在表中插入几行数据
data = [('Richard Lucas', 'Note', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]

# 文号在这里用作占位符，表示你想在SQL命令中使用的值。在连接对象的execute
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# 查询sales表
# 使用execute()方法运行一条SQL命令，并将命令结果赋给一个光标对象cursor。
cursor = con.execute("SELECT * FROM sales")
# fetchall()方法取出结果集中的所有行
rows = cursor.fetchall()

# 计算查询结果中行的数量
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: %d' % (row_counter))