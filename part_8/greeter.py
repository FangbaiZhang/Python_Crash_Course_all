#_*_coding:cp936_*_
# ����һ������
# ��ϸ˵������P114

def greet_user():
    '''��ʾ�򵥵��ʺ���'''
    print("Hello!")

greet_user()

def greet_user(username):
    # ��ʾ�򵥵��ʺ���
    print("Hello! " + username.title() + "!")

greet_user('jessle')
greet_user('felix')
