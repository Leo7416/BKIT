import unittest
from main import *

task_1_result = [
    ('Азов', 500, 'Города'), ('Псков', 450, 'Города')
]

task_2_result = [
    ('Аппартаменты', 875), ('Доход', 800), ('Города', 475)
]

task_3_result = [
    ('Аппартаменты', ['Здания', 'Сады'])
]

class RK_test(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task_1_result, task_1())

    def test_task_2(self):
        self.assertEqual(task_2_result, task_2())

    def test_task_3(self):
        self.assertEqual(task_3_result, task_3())