# coding=utf-8
# ��ϸ˵������P130

# ʹ��λ��ʵ�κʹ�������������ʵ�Σ����ʹ��

def make_pizza(size, *toppings):
    """print all toppings"""
    print("\nMaking a " + str(size) + 
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



