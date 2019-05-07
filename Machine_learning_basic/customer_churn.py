import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv('./data/churn.csv', sep=',', header=0)
# 将列标题中的空格替换成下划线，并删除嵌入的单引号；strip函数出去了列标题Churn?末尾的文号。lower()函数将所有列标题转换为小写
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ','_').str.replace('\'','').str.strip('?')]

# 创建一个新列 churn01，并使用numpy的where函数根据churn这一列中的值用1或0来填充它。
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

# head函数显示标题行和前5个数据行
print(churn.head())

# 为分组数据计算描述性统计量
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))

# 为不同的变量计算不同的统计量
print(churn.groupby(['churn']).agg({'day_charge' : ['mean', 'std'],
                                    'eve_charge' : ['mean', 'std'],
                                    'night_charge' : ['mean', 'std'],
                                    'intl_charge' : ['mean', 'std'],
                                    'account_length' : ['count', 'min', 'max'],
                                    'custserv_calls' : ['count', 'min', 'max']}))


