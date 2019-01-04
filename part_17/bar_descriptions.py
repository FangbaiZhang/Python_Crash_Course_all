# -*- coding: cp936 -*-
# ��ϸ��P347
# ��ͼ������Զ��幤����ʾ

import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#993366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 30
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

# ���б��е��ֵ䴫�ݸ�Y���꣬�ֵ�ĵ�һ������Ӧ��ֵΪY���꣬�ڶ�������ֵ��Ϊ������ʾ
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of django'},
    {'value': 14798, 'label': 'Description of flask'},
    ]
    
chart.add('Star', plot_dicts)
chart.render_to_file('bar_descriptions.svg')


 

