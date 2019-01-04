# -*- coding: cp936 -*-
# ���Ƽ򵥵�����ͼ
# ����plot�ṩ����ʱ��Ĭ�����ݵ�һ��ֵ��Ӧ��x����Ϊ0�����Ի�����ͼ��1��Ӧ��xΪ0
# 25��Ӧ��xΪ4����������1����һ��ֵ��0
# ��������2��ͬʱ��������ֵ�����ֵ

import matplotlib.pyplot as plt

squares = [1, 4, 9 , 16, 25]
plt.plot(squares, linewidth=5)

# ����ͼ����⣬������������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', labelsize=14)

plt.show()


# ��������1

squares = [0, 1, 4, 9 , 16, 25]
plt.plot(squares, linewidth=5)

# ����ͼ����⣬������������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', labelsize=14)

plt.show()


# ��������2

input_values = [1, 2, 3, 4 , 5]
squares = [1, 4, 9 , 16, 25]
plt.plot(input_values, squares, linewidth=5)

# ����ͼ����⣬������������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', labelsize=14)

plt.show()



