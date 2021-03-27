import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.api import  *


pro = ts.pro_api('填自己的token')#https://tushare.pro/ 注册账号填自己的token
data = pro.daily(ts_code='600848.SH', start_date='20180101', end_date='20210327')#ts_code是股票代码  start_date是开始时间 end_date结束时间

#如果要预测btc之类的虚拟货币可以查看https://tushare.pro/  官网的发布的比特币数据

data.index = pd.to_datetime(data['trade_date'])
print(data)
lst = data.index.tolist()


arma = tsa.ARMA(data[['high']],(1,1))
model = arma.fit()
predict = model.predict(1,lst[-1])

figure = plt.figure('股票曲线',figsize=(50,4))
ax = figure.add_axes([0.1,0.1,0.8,0.8],xlabel='日期',ylabel='价格')
ax.plot(data[['high']],color=(1,0,0,1),label='真实价格')
ax.plot(predict,color=(0,0,1,1),label='预测价格')
plt.legend()
plt.show()