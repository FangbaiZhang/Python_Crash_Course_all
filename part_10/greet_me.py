# -*- coding: cp936 -*-
# ʹ��json.dump()�洢����

import json

filename = 'username.json'
with open(filename) as f_obj:
   username = json.load(f_obj)
   print("Welcome back, " + username + "!")
   




    
