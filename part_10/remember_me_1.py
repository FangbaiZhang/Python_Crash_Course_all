# -*- coding: cp936 -*-
# �ع�����

import json

def get_stored_username():
    """����洢���û������ͻ�ȡ��"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """��ʾ�û������û���"""
    username = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """�ʺ��û�����ָ��������"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remeber you when you come back, " + username + "!")
    
greet_user()
    
   




    
