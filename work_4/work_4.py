from efficient_apriori import apriori
import numpy as np
import pandas as pd

#数据无表头，故设读取参数header=None
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
#对数据进行处理，遍历每个数据将有效数据保存到transaction
transaction = []
for i in range(0,dataset.shape[0]):
    temp=[]
    for j in range(0,dataset.shape[1]):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(str(dataset.values[i,j]))
    transaction.append(temp)
#列出频繁项集和频繁规则
itemsets, rules = apriori(transaction, min_support=0.05, min_confidence=0.2)
print('频繁项集：',itemsets)
print('关联规则: ',rules)
