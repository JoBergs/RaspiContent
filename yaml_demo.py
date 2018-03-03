#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/ [ARTICLE!]
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import yaml

data = {'content': {'size': 15, 'tag': 'main'}}

with open('config.yaml', 'w') as f:
    yaml.dump(data, f)

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    print(config['content'])
