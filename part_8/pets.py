# coding=utf-8
# ��λ�ô���ʵ��
# ��ϸ˵������P116

# λ��ʵ��
def describe_pet(animal_type, pet_name):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
    
# �ؼ���ʵ��
def describe_pet(animal_type, pet_name):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# Ĭ��ֵ����������Ĭ��Ϊ��
def describe_pet(pet_name, animal_type = 'dog'):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name = 'harry')


