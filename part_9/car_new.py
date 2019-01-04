# -*- coding: cp936 -*-
# ��ϸ˵������P153

"""һ�������ڱ�ʾ��������"""

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

class Battery():
    """һ��ģ��綯������ƿ�ļ򵥳���"""
    
    def __init__(self, battery_size=70):
        """��ʼ����ƿ������"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """��ӡһ����Ϣ������ƿ������"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """��ӡһ����Ϣ��ָ����ƿ���������"""
        if self.battery_size == 70:
            range = 240
        else: 
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """�綯�����Ķ���֮��"""
    
    def __init__(self, make, model, year):
        """��ʼ�����������,�ٳ�ʼ���綯��������������"""
        super().__init__(make, model, year)
        self.battery = Battery()
