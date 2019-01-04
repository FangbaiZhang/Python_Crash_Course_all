# -*- coding: cp936 -*-
# ����һϵ�е��ɢ��ͼ���Զ���������
# ��ϸ��P294
# ʹ��RGB����ͼ����ɫ,������ɫc����0-1��ֵ���ֱ��ʾ��������ֵΪ1��0,0���Ǻ�ɫ
# ֵԽ�ӽ���1��ɫԽ��
# ʹ����ɫӳ��

import matplotlib.pyplot as plt

# ���ƶ����

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

# ��ɫӳ�䣬��c���ó�x����y��ֵ��Ȼ������cmapӳ�䣬ֱ�ӽ�matplotlib����ѡ����ɫ���������
# Colormap reference��ַ��https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet, 
        edgecolor='none', s=50)

# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='both', colors='blue', labelsize=14)

# ����ÿ���������ȡֵ��Χ
plt.axis([0, 1050, 0, 1100000])

plt.show()


