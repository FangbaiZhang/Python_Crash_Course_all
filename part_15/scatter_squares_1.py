# -*- coding: cp936 -*-
# ����һϵ�е��ɢ��ͼ��������ʽ

import matplotlib.pyplot as plt

# ���ƶ����

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='both', colors='blue', labelsize=14)

plt.show()

