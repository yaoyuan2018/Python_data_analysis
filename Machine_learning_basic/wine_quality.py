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