# coding=utf-8
# ��ϸ˵������P125

# ����ֵΪ�ֵ�
def city_country(city, country):
    """return to full name"""
    full_name = city + ', ' + country
    return full_name.title()


aaa = city_country('santiago', 'chile')
print(aaa)

