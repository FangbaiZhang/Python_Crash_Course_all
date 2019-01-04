# -*- coding: cp936 -*-

#�����
import matplotlib.pyplot as plt
import numpy as np
#֧��������ʾ
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
 
#��������
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
 
#����figure����
plt.figure(num=3, figsize=(8, 5))
#������1
plt.plot(x, y1)
#������2
plt.plot(x, y2, color='blue', linewidth=5.0, linestyle='--')
#���������᷶Χ
plt.xlim((-5, 5))
plt.ylim((-2, 2))
#��������������
plt.xlabel('xxxxxxxxxxx')
plt.ylabel('yyyyyyyyyyy')
#����������̶�
my_x_ticks = np.arange(-5, 5, 0.5)
my_y_ticks = np.arange(-2, 2, 0.3)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
 
#��ʾ����������
plt.show()
