import matplotlib.pyplot as plt
import numpy as np
import time
import random
import matplotlib.style as mplstyle
mplstyle.use('fast')

a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)       #设置开始日期时间元组（1976-01-01 00：00：00）
a2 = (1990, 12, 31, 23, 59, 59, 0, 0, 0)  #设置结束日期时间元组（1990-12-31 23：59：59）
start=time.mktime(a1)  #生成开始时间戳
end=time.mktime(a2)   #生成结束时间戳
#随机生成10个日期字符串
x = []
for i in range(5):
  t=random.randint(start,end)  #在开始和结束时间戳中随机取出一个
  date_touple=time.localtime(t)     #将时间戳生成时间元组
  date=time.strftime("%Y-%m-%d", date_touple) #将时间元组转成格式化字符串（1976-05-21）
  x.append(date)




y = np.linspace(0, 2, 5)

plt.plot(x, y, label='linear')
plt.plot(x, y*2, label='quadratic')
plt.plot(x, y*3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")


plt.legend()
plt.show()
