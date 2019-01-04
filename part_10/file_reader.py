# -*- coding: cp936 -*-

# ��ͬһ���ļ����µ��ĵ�
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# ���þ���·�����ĵ���������б�ܣ�����򿪴��󻻳ɷ�б��
file_path = 'C:/Users/HP/Desktop/python_work/part_10/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# ���ļ�����ÿ��һ�еķ�ʽ����ļ�
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)

# ���ļ�����ÿ��һ�еķ�ʽ����ļ���print������Ҳ��һ�����з�,Ĭ���ļ�ĩβ��һ�����з�
# ʹ��rstrip()�����������з�
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# ���ļ������ּ��
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object.read():
        print(line.rstrip())

# ���򿪵ĸ��д洢��һ���б��У����ҿ�����with�����֮��ʹ������б�
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
        print(line.rstrip())
