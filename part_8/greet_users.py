# coding=utf-8
# ��ϸ˵������P126

# �����б�ʹ�ú����ʺ��б��е�ÿһ����
def greet_users(names):
    """greet to everyone"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


