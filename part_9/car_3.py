# -*- coding: cp936 -*-
# ��ϸ˵������P144
# ����һ����������
# �޸����Ե�ֵ�����ֲ�ͬ�ķ���
# ����2��ͨ���������ڲ��������Ե�ֵ,���һ���߼�����ֹ����̸�С

class Car():
    
    def __init__(self, make, model, year):
        """��ʼ����������������"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20
    
    def get_descriptive_name(self):
        """�����������������Ϣ"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """��ӡ��һ��ָ��������̵���Ϣ"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """����̱��������Ϊָ����ֵ,��ֹ����̱������ص�"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(19)
my_new_car.read_odometer()


