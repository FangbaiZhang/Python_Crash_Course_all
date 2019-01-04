# -*- coding: cp936 -*-

# ����һ��������ͳ��һ���ĵ��ж��ٸ�����

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','sidd.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)

# �������г��ִ���ʱ��ʲô������������������ʣ��Ĵ��룬ʹ��pass
print("\n")
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','sidd.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)
