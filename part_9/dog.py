# -*- coding: cp936 -*- 
# -*- coding: utf-8 -*-

# ��ϸ˵������P139
# ����һ��С������


class Dog():
    """һ��ģ��С���ļ򵥳���"""
    
    def __init__(self, name, age):
        """��ʼ������name��age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """ģ��С������ʱ����"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """ģ��С������ʱ���"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('wille', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()

