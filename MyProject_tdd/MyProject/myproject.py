#!/usr/bin/python
#encoding: utf-8

class MyProject(object):
    def covered_method(self):
    	""" Method covered by coverage. """
        print 'Covered by test framework.'
        return 1

    def uncovered_method(self):
        print 'Not covered by test framework.'

if __name__ == '__main__':
    myproject = MyProject()
    myproject.covered_method()
    myproject.uncovered_method()
