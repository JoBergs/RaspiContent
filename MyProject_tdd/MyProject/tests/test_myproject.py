#encoding: utf-8
from unittest import TestCase

from MyProject import MyProject

class MyProjectTestCase(TestCase):
    def test_covered_method(self):
        project = MyProject()
        assert project.covered_method() == 1

    def test_failed_test(self):
        assert 1 == 2
