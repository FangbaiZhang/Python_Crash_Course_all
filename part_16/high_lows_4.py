# -*- coding: cp936 -*-
# ��ϸ��P322
# ����CSV�ļ�,��ȡ���ڣ�������£��������
# ��������쳣���ݵ��ļ������ڿ��ַ������ļ�

import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'death_valley_2014.csv'
with open(filename) as f:
    
    # ��ȡ�����ļ�������
    reader = csv.reader(f)
    
    # ��ȡ�ļ��ĵ�һ������
    header_row = next(reader)

    # ��ӡ�ļ�ͷ����λ�ã������ǵڼ��У������Ӧ������


    # ���������ʾ��ȡ�ļ��е�������£����������ʾ����0��Ϊ���ڣ���һ��Ϊ�������    
    dates, highs, lows = [], [], []
    for row in reader: # �ӵ�2�п�ʼ����ÿһ�У���Ϊ��һ��ǰ���Ѿ�����next��ȡ��
        # ʹ��try-except-else����鴦��ȱ�����ݵ�����
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)  
            lows.append(low)


# ��������������ݻ���ͼ��
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, linewidth=2, ls='-')
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1, ls='-')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# ����ͼ�εĸ�ʽ
title = "Daily high and low temperature - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.ylim(10, 120) # ����y�����귶Χ

#���������᷶Χ���̶�
my_y_ticks = np.arange(10, 120, 10)
plt.yticks(my_y_ticks)

fig.autofmt_xdate() # ��x�������б����ʾ
plt.tick_params(axis='both', which='both', width=2, 
        colors='black', direction='in', labelsize=8)


plt.show()
            

