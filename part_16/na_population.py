# -*- coding: cp936 -*-
# ��ϸ��P329
# ���������ͼ���ڵ�ͼ����ʾ��������
# ��ʾ�������ҵ��˿�����

import pygal 
import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})

wm.render_to_file('na_population.svg')

