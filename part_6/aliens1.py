# coding=utf-8
# Ŀ�ģ��б��д洢�ֵ䣬ͬʱ�޸������˵���ɫ

# ����һ�����ڴ洢�����˵Ŀ��б�
aliens = []

# ����30����ɫ������
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# �޸�ǰ���������˵���ɫ
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# ��ʾǰ5�������ˣ���ǰ3���Ƿ��Ѿ��޸�
for alien in aliens[0:5]:
    print(alien)
print("...")

# ������չ���ѭ������ǰ3���������޸�Ϊ��ɫ
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("...")
        





