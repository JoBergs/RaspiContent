#!/usr/bin/python
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/python-project-setup-test-driven-development/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

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
