# -*- coding: cp936 -*-
# ��ϸ��P345
# ִ��API���ã��ҳ�GitHub��������ߵ���Ŀ

import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# ִ��API���ò��洢��Ӧ
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# ��ӡһ��״̬�룬��������ַ�Ƿ�ɹ�
print("Status code:", r.status_code)

# ��ȡ������ַ��Ϣ����ʵ����һ�������ֵ����Ϣ����API��Ӧ�洢��һ���ֵ���
response_dict = r.json()
# ������,��ӡ����ȡ�ĵ��ֵ��еļ�������ҳ�Աȣ�����û������
print(response_dict.keys())
print("Total repositories:", response_dict['total_count']) # ��ӡ����Ŀ

# ̽���йزֿ����Ϣ,items��Ӧ����һ���б��б��а����ܶ��ֵ�
repo_dicts = response_dict['items']

# ���ӻ��ֿ����Ϣ,���ֿ����ƺͶ�Ӧ������ȡ���б���
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#993366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 30
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('Stars', stars)
chart.render_to_file('Python_repos_1.svg')


 

