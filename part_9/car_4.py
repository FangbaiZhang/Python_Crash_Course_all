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
        self.odometer_reading = 0
    
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
        
    def increment_odometer(self, miles):
        """����̱��������ָ�������"""
        if miles >= 0:
            self.odometer_reading += miles
        else :
            print("You can't roll back an odometer!")

my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


