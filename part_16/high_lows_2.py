# -*- coding: cp936 -*-
# ��ϸ��P318
# ����CSV�ļ�

import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    
    # ��ȡ�����ļ�������
    reader = csv.reader(f)
    
    # ��ȡ�ļ��ĵ�һ������
    header_row = next(reader)

    # ��ӡ�ļ�ͷ����λ�ã������ǵڼ��У������Ӧ������
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # ���������ʾ��ȡ�ļ��е�������£����������ʾ����0��Ϊ���ڣ���һ��Ϊ�������    
    dates, highs = [], []
    for row in reader: # �ӵ�2�п�ʼ����ÿһ�У���Ϊ��һ��ǰ���Ѿ�����next��ȡ��
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)  # ��ÿ�е�����1�������ݣ�ʵ��Ϊ���ĵڶ������������ӵ��б���

# ��������������ݻ���ͼ��
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# ����ͼ�εĸ�ʽ
plt.title("Daily high temperature, 2014")
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate() # ��x�������б����ʾ
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='minor', which='both', width=2, 
        colors='gold', direction='in', labelsize=8)

plt.show()
            

