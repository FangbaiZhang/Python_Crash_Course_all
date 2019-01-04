# -*- coding: cp936 -*-
# ����һϵ�е��ɢ��ͼ���Զ���������
# ��ϸ��P295
# ʹ����ɫӳ��

import matplotlib.pyplot as plt

# ���ƶ����

x_values = list(range(1, 30))
y_values = [x**3 for x in x_values]

# ��ɫӳ�䣬��c���ó�x����y��ֵ��Ȼ������cmapӳ�䣬ֱ�ӽ�matplotlib����ѡ����ɫ���������
# Colormap reference��ַ��https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet, 
        edgecolor='none', s=50)

# ����ͼ�����Ⲣ����������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='both', labelsize=14)

# ����ÿ���������ȡֵ��Χ
plt.axis([0, 32, 0, 30000])

plt.show()

