# -*- coding: cp936 -*-
# ��ϸ��P3451
# ִ��API���ã��ҳ�Hacker News���ŵ�����

import requests
import pygal 
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# ִ��API���ò��洢��Ӧ
url = 'https://hacker-news.firebaseio.com/v0/'
r = requests.get(url)
print("Status code:", r.status_code)




 

