# -*- coding: cp936 -*-
# ʹ��json.dump()�洢����

import json

numbers = [1, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    




    
