# -*- coding: cp936 -*-

import numpy as np
import matplotlib.pyplot as plt
#�����Ա�������
x= np.linspace(0,2*np.pi,500)
#��������ֵ����
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x*x)
#����ͼ��
plt.figure(1)
'''
��˼����һ��2��2�й�4����ͼ��ͼ�У���λ��1��ͼ�����в�������ͼ����
������Ǹ�1��ʾ��1����ͼ���Ǹ����ֵı仯����λ��ͬ����ͼ
'''
#��һ�е�һ��ͼ��
ax1 = plt.subplot(2,2,1)
#��һ�еڶ���ͼ��
ax2 = plt.subplot(2,2,2)
#�ڶ���
ax3 = plt.subplot(2,1,2)
#ѡ��ax1
plt.sca(ax1)
#���ƺ�ɫ����
plt.plot(x,y1,color='red')
#����y�����᷶Χ
plt.ylim(-1.2,1.2)
#ѡ��ax2
plt.sca(ax2)
#������ɫ����
plt.plot(x,y2,'b--')
plt.ylim(-1.2,1.2)
#ѡ��ax3
plt.sca(ax3)
plt.plot(x,y3,'g--')
plt.ylim(-1.2,1.2)
plt.show()

