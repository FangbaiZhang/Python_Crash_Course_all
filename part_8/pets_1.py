# coding=utf-8
# ��λ�ô���ʵ��
# ��ϸ˵������P119

# λ��ʵ�Ρ��ؼ���ʵ�κ�Ĭ��ֵ���Ի��ʹ��
def describe_pet(pet_name, animal_type = 'dog'):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# һ����ΪWillie��С��(�������ַ�ʽ������һ��)
# λ��ʵ�κ͵���Ĭ��ֵ
describe_pet('willie')

# �ؼ���ʵ�κ͵���Ĭ��ֵ
describe_pet(pet_name = 'willie')

# һֻ��ΪHarry�Ĳ���(ʵ�λ���)(�������ַ�ʽ������һ��)
# λ��ʵ���滻Ĭ��ֵ
describe_pet('harry', 'hamster')

# �ؼ���ʵ��
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# �ؼ���ʵ��λ�õ���
describe_pet(animal_type = 'hamster', pet_name = 'harry')





