# -*- coding: cp936 -*-
# ��ϸ˵������P142
# ����һ���û�����

class User():
    
    def __init__(self, first_name, last_name, age, country):
        """��ʼ���û�����Ϣ"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    
    def describe_user(self):
        """����������û���Ϣ"""
        print("The user's name is " + self.first_name.title()
                + " " + self.last_name.title() + ".")
        # �漰�����֣�ת���ɿ�����ʾ��ֵ����סʹ��str����
        print("The user's age is " + str(self.age) + ", and come from " 
                + self.country)
    
    def greet_user(self):
        print("Hello, " + self.first_name.title()
                + " " + self.last_name.title() + ".")
                
user_1 = User('felix', 'zhang', 28, 'China')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Kobb', 'zhang', 20, 'America')
user_2.describe_user()
user_2.greet_user()

        
        
                
 


