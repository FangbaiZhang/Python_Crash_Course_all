# coding=utf-8
# Ŀ�ģ�����30����ɫ������

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#����һ�����ڴ洢�����˵Ŀ��б�
aliens = []

#����30����ɫ��������
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#��ʾǰ5��������
for alien in aliens[:5]:
    print(alien)
print("...")

#��ʾ�����˶��ٸ�������
print("Total number of aliens: " + str(len(aliens)))

