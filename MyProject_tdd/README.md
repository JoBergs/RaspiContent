myproject
===========

Installation:
--------
wget https://github.com/JoBergs/RaspiContent/raw/master/MyProject_tdd.zip
unzip MyProject_tdd.zip
wget http://www.raspython.org/wp-content/uploads/2015/03/get-pip.py_.zip
unzip get-pip.py_.zip
sudo python get-pip.py
cd MyProject_tdd
sudo pip install -r requirements.txt
cd MyProject

About:
--------

Enter Readme here!

This class does something very useful:

    class MyProject(object):
        def covered_method(self):
            print 'Covered by test framework.'

Start the application:
--------

    $ cd ~/MyProject_tdd/MyProject
    $ sudo python myproject.py

Testing:
--------

    $ cd ~/MyProject_tdd
    $ sudo py.test -x -s --cov-report html --cov MyProject MyProject/tests/test_myproject.py

In the hosts terminal, copy the directory ./htmlcov/ from the Raspberry Pi and open it in firefox:

    $ scp -r pi@RASPBERRY_IP:/home/pi/MyProject_tdd/htmlcov /home/YOUR_USER_NAME/
    $ firerox /home/YOUR_USER_NAME/htmlcov/index.html

Sphinx Documentation:
-------------------

    $ cd ~/MyProject_tdd
    $ make html

Then, open your browser and go to ./_build/index.html

Update package version::
-------------

Update the version number in setup.py, then

    $ python setup.py sdist
