# -*- coding: cp936 -*-

# �Բ�ͬ�ķ�ʽ���ļ�������ʾ������


file_name = "learning_python.txt"

# ����1��ȫ����ȡ��
with open(file_name) as file_object:
    content = file_object.read()
    print(content)
    
# ����2��һ�δ�һ��
with open(file_name) as file_object:
    content = file_object.readline()
    print(content)

# ����ѭ���ķ�ʽ�����δ�ÿһ��
with open(file_name) as file_object:
    while True:
        content = file_object.readline()
        print(content)
        if not content:
            break
            
# ����3��ÿ��һ�еķ�ʽ��ȡ�����ļ�������ÿ����Ϊһ��Ԫ�ش洢��һ���б���
# ���Բ���forѭ����ȡ�б��е�����Ԫ��
with open(file_name) as file_object:
    contents = file_object.readlines()
    print(contents)

pi_string = ''
for content in contents:
    pi_string += content.strip()

print(pi_string)
pi_string.replace('love','hate')
print("\n" + pi_string)



# ����4������fileinputģ��
import fileinput
for line in fileinput.input("learning_python.txt"):
    print(line)



       
aaa = "www.w3cschool.cc"
print ("����̳̾ɵ�ַ��", aaa)
print ("����̳��µ�ַ��", aaa.replace("w3cschool.cc", "runoob.com"))

aaa = "this is string example....wow!!!"
print (aaa.replace("is", "was", 3))  


aaa = "I reallly like dogs."
aaa = aaa.replace("dogs", "cats")
print (aaa) 

