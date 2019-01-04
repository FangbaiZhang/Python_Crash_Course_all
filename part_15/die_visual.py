# -*- coding: cp936 -*-
# ��ϸ��P305
# Ͷ������

import pygal
from die import Die

# ����һ��D6ʵ��
die = Die()

# Ͷ���������ӣ���������洢��һ���б���
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# print(results)

# ��������������ֳ��ֵ�����
frequencies = []
for value in range(1, die.num_sides+1):
    # count��������ͳ��һ��ֵ���б��г��ֵĴ���
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# �Խ�����п��ӻ�

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')



            

