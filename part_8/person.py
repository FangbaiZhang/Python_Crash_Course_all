# coding=utf-8
# ��ϸ˵������P123

# ����ֵΪ�ֵ�
def build_person(first_name, last_name):
    """return to a dictionary, include a person's information"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# ����ֵΪ�ֵ�,�����ѡ�β����䣬age��ֵʱ����age���뵽�ֵ���
def build_person(first_name, last_name, age = ''):
    """return to a dictionary, include a person's information"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

