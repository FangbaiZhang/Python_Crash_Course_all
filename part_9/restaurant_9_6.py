# -*- coding: cp936 -*-
# ��ϸ˵������P142
# ����һ���͹ݵ���

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type, open_time, favors):
        """��ʼ����͹ݵ�����"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_time = open_time
        self.favors = favors
    
    def describe_restaurant(self):
        """�����������������Ϣ"""
        print("The restaurant's name is " + self.restaurant_name)
        print("The cuisine_type is " + self.cuisine_type)
    
    def open_restaurant(self):
        if self.open_time >= 10:
            print("The restaurant has opened.")
        else:
            print("The restaurant has closed.")
    
    
        



new_restaurant = Restaurant('Yunxi', 'Chuancai', 20, 'Sweet')
new_restaurant.describe_restaurant()

        
        
                
 


