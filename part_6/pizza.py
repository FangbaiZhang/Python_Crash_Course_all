# coding=utf-8
# Ŀ�ģ��ֵ��д洢�б�

#�洢������������Ϣ
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'exttra cheese'],
    }

# �������������
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# ��ʾÿ����ϲ��������
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
print(favorite_languages)

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# ����if��䣬�ı������ʽ
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }


for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s favorite languages is " + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
