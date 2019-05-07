import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

# 将数据集读入到pandas数据框中,参数表示域分隔符为逗号，第一行为列标题。
wine = pd.read_csv('data/wine-merge.csv', sep=',', header=0)

# 有些标题中包含空格，例如：fixed acidity，所以使用下划线替换空格。
wine.columns = wine.columns.str.replace(' ','_')

# 使用head函数检查一下标题行和前5含数据，确保数据被正确加载。
print(wine.head())

# 显示所有变量的描述性统计量，使用describe函数打印出数据集中每个数值型变量的摘要统计量。
# 包括：总数、均值、标准差、最小值、第25个百分数、中位数、第75个百分位数和最大值。
print(wine.describe())

# 识别质量列中的唯一值，并以升序打印在屏幕上。
print(sorted(wine.quality.unique()))

# 计算质量列中每个唯一值在数据集中出现的次数，并把它们以降序打印到屏幕上。
print(wine.quality.value_counts())

# 按照葡萄酒类型显示质量的描述性统计量
print(wine.groupby('type')[['quality']].describe().unstack('type'))

# 按照葡萄酒类型显示质量的特定分位数值
print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))

# 按照葡萄酒类型查看质量分布

red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']
sns.set_style("dark",{'font.sans-serif':['SimHei'],'font.serif':['SimHei']})
print(sns.distplot(red_wine,norm_hist=True, kde=False, color="red", label=u"红葡萄酒"))
print(sns.distplot(white_wine,norm_hist=True, kde=False, color="white", label=u"白葡萄酒"))

#sns.axlabel("Quality Score", "Density")
plt.title("红/白葡萄酒的质量分布图")
plt.legend()
plt.show()

# 检验红葡萄酒和白葡萄酒的平均质量是否有所不同

print(wine.groupby(['type'])[['quality']].agg(['std']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))

# corr函数可以计算出数据集中所有变量两两之间的线性相关性。
print(wine.corr())

# 从红葡萄酒和白葡萄酒的数据中取出一个“小”样本来进行绘图，定义take_sample函数抽取在统计图中使用的样本点。
def take_sample(data_frame, replace=False, n=200):
    # random.choice函数随机选择一个行的子集
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
# 对红葡萄酒数据进行抽样
reds_sample = take_sample(wine.loc[wine['type']=='red', :])
# 对白葡萄酒数据进行抽样
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
# 将抽样所得的两个数据框连接在一起
wine_sample = pd.concat([reds_sample, whites_sample])

# 在wine数据框中创建一个新的列in_sample,并使用numpy的where函数和pandas的isin函数对这个新列进行填充,填充的值根据此行的索引值是否在抽样数据的索引值中分别设为1和0.
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index),1.,0.)

# 使用pandas的crosstab函数来确认in_sample列中包含400个1和6097个0
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

# 查看成对变量之间的关系
sns.set_style("dark")
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False,"x_jitter": 0.25, "y_jitter": 0.25}\
                 , hue='type', diag_kind='hist',diag_kws={"bins": 10, "alpha": 1.0},\
                 palette=dict(red="red", white = "white"),\
                 markers=['o', 's'], vars=['quality','alcohol','residual_sugar'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize = 14,\
             horizontalalignment='center', verticalalignment='top',x=0.5, y=0.999)
plt.show()

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density \
             + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates\
             + total_sulfur_dioxide + volatile_acidity'

# 最小二乘法进行线性拟合
lm = ols(my_formula, data=wine).fit()

## 或者，也可以使用广义线性模型（glm）语法进行线性回归
## lm = glm(my_formula, data = wine, family = sm.families.Gaussian()).fit()

# 打印结果的摘要信息，包含了模型系数、系数的标准差和置信区间、修正R方、F统计量等模型详细信息。
print(lm.summary())

# 打印一个列表，其中包含从模型对象lm中提取出的所有数值信息
print("\nQuantities you can extract from the result:\n %s" % dir(lm))

# lm.params以一个序列的形式返回模型系数，这样你可以通过定位或名称提取出单个的系数。
print("\nCoefficients:\n%s" % lm.params)

# lm.bse以序列的形式返回模型系数的标准差。
print("\nCoefficient Std Errors: \n%s" % lm.bse)

# lm.rsquared_adj返回修正R方
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)

# lm.fvalue和lm.f_pvalue分别返回F统计量和它的p值。
print("\nF-statistic: %.1f    P-value: %.2f" % (lm.fvalue, lm.f_pvalue))

# lm.fittedvalues返回拟合值
print("\nNumber of obs: %d    Number of fitted values: %d" % (lm.nobs,\
                                                              len(lm.fittedvalues)))

# 创建一个名为dependent_variable的序列来保存质量数据
dependent_variable = wine['quality']

# 创建一个名为independent_variables的数据框
# 来保存初始的葡萄酒数据集中除quality、type和in_sample之外的所有变量
independent_variables = wine[wine.columns.difference(['quality','type','in_sample'])]

# 对自变量进行标准化
# 对每个变量，在每个观测中减去变量的均值
# 并且使用结果除以变量的标准差
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()

# 将因变量quality作为一列添加到自变量数据框中
# 创建一个带有标准化自变量的
# 新数据集
wine_standardized = pd.concat([dependent_variable, independent_variables_standardized], axis=1)

# 完成了带有标准化自变量的数据集后，重新进行线性回归，并查看一下摘要统计
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())


# 使用葡萄酒数据集中的前10个观测创建10个“新”观测
# 新观测中只包含模型中使用的自变量
new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]

# 基于新观测中的葡萄酒特性预测质量评分
y_predicted = lm.predict(new_observations)

# 将预测值保留两位小数并打印到屏幕上
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)