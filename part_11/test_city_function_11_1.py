# -*- coding: cp936 -*-
# ���Դ���

import unittest
from city_functions_11_1 import get_city_name

class NamesTestCase(unittest.TestCase):
    """����name_function_1.py"""
    
    def test_city_name(self):
        """�ܹ���ȷ�Ĵ�����Janis Joplin������������"""
        city_name = get_city_name('chengdu', 'China')
        self.assertEqual(city_name, 'Chengdu China')
    

unittest.main()


