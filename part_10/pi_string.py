# -*- coding: cp936 -*-

# ʹ�ô��ļ��е�ֵ
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

# �ȶ�ȡ��һ�У�pi_string�͵��ڵ�һ���ַ�����Ȼ���ȡ�ڶ��У��ӵ�����ַ����ϣ�ֱ��ѭ������
pi_string = ''    
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# ɾ�����еĿո����ʹ��strip()
pi_string = ''    
for line in lines:
    pi_string += line.strip()

print("\n" + pi_string)
print(len(pi_string))

# ���򿪵��ļ��洢��һ���б��У������֮�󻹿���ʹ��
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print("\n" + line.rstrip())



