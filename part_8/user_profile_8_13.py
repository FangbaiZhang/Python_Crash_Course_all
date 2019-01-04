# coding=utf-8
# ��ϸ˵������P132

# ʹ�����������Ĺؼ���ʵ��,����**

def build_profile(first, last, **user_info):
    """print all information"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', 
                            location = 'princeton', 
                            field = 'physics',
                            country = 'china',
                            city = 'chengdu')
print(user_profile)



