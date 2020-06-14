import pandas as pd
result=pd.read_csv('car_complain.csv')
result=result.drop(columns='problem').join(result['problem'].str.get_dummies(','))
print(result)
tags=result.columns[7:]
df1=result.groupby('brand')['id'].agg(['count'])
print('品牌投诉总数排名：',df1.sort_values('count',ascending=False))
df2=result.groupby('car_model')['id'].agg(['count'])
print('车型投诉总数排名',df2.sort_values('count',ascending=False))
df3=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby('brand').mean()
print('平均车型投诉数品牌排名',df3.sort_values('count',ascending=False))



