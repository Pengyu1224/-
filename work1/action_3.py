import pandas as pd
result=pd.read_csv('car_complain.csv')
result=result.drop(columns='problem').join(result['problem'].str.get_dummies(','))#去除problem列，然后以逗号分隔不同问题代码然后作为列加入到原dataframe中
df1=result.groupby('brand')['id'].agg(['count'])#按品牌分组后以投诉统计次数聚类
print('品牌投诉总数排名：',df1.sort_values('count',ascending=False))
df2=result.groupby('car_model')['id'].agg(['count'])#按车型分组后以投诉统计次数聚类
print('车型投诉总数排名',df2.sort_values('count',ascending=False))
df3=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby('brand').mean()#按车型和品牌分组然后按统计次数聚类，然后再按照品牌分组并计算各品牌投诉统计次数平均值
print('平均车型投诉数品牌排名',df3.sort_values('count',ascending=False))



