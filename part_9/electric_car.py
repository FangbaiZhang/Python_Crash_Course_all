# -*- coding: cp936 -*-
# ��ϸ˵������P148
# ��ļ̳�


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

class ElectricCar(Car):
    """�綯�����Ķ���֮��"""
    
    def __init__(self, make, model, year):
        """��ʼ�����������,�ٳ�ʼ���綯��������������"""
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """��ӡһ����Ϣ������ƿ������"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(20)
my_tesla.read_odometer()
my_tesla.describe_battery()

