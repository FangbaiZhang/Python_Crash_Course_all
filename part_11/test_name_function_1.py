# -*- coding: cp936 -*-
# ���Դ���

import unittest
from name_function_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """����name_function_1.py"""
    
    def test_first_last_name(self):
        """�ܹ���ȷ�Ĵ�����Janis Joplin������������"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """�ܹ���ȷ�Ĵ�����Janis Joplin������������"""
        formatted_name = get_formatted_name('janis', 'joplin', 'felix')
        self.assertEqual(formatted_name, 'Janis Felix Joplin')


unittest.main()


