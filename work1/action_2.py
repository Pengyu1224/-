import numpy as np
persontype=np.dtype({'names':['name','Chinese','Math','English'],'formats':['S32','i','i','i']})#定义数据类型
peoples=np.array([('Zhangfei',68,65,30),('Guanyu',95,76,98),('Liubei',98,86,88),('Dianwei',90,88,77),('Xuchu',80,90,90)],dtype=persontype)
#提取各项成绩
ChineseScore=peoples[:]['Chinese']
MathScore=peoples[:]['Math']
EnglishScore=peoples[:]['English']
print('语文、数学、英语平均成绩分别为：',np.mean(ChineseScore),np.mean(MathScore),np.mean(EnglishScore))
print('语文、数学、英语最好成绩分别为：',np.max(ChineseScore),np.max(MathScore),np.max(EnglishScore))
print('语文、数学、英语最差成绩分别为：',np.min(ChineseScore),np.min(MathScore),np.min(EnglishScore))
print('语文、数学、英语成绩方差分别为：',np.var(ChineseScore),np.var(MathScore),np.var(EnglishScore))
print('语文、数学、英语成绩标准差分别为：',np.std(ChineseScore),np.std(MathScore),np.std(EnglishScore))
ranking=sorted(peoples,key=lambda x:x[1]+x[2]+x[3],reverse=True)#根据条件排序
print('成绩排名为：',ranking)
