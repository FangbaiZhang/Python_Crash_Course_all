# -*- coding: cp936 -*-
# ����ɢ��ͼ��������ʽ

import matplotlib.pyplot as plt

# ���Ƶ�����

plt.scatter(2, 4, s=200)

# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

