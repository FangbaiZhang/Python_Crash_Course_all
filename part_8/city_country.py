# coding=utf-8
# ��ϸ˵������P125

# ����ֵΪ�ֵ�
def get_formatted_name(first_name, last_name):
    """return to full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

