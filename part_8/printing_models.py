# coding=utf-8
# ��ϸ˵������P127

# ����������������ӡ�б���ʾ�б�
# ��ӡÿ����ƣ��������ƶ�������һ���б���

def print_models(unprinted_designs, completed_models):
    """print every designs, and then been moved to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #ģ��3D��ӡģ�͵Ĺ���
        print("Printing modeling: " + current_design)
        completed_models.append(current_design)

# ����һ����ʾ��ӡ������ģ�͵ĺ���
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# ���²���Ϊ������ֻ��Ҫ���ú�������

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# ������Ƭ[:]���������б�����ԭ�б���Ȼ����
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)




