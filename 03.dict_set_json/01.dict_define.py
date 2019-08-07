#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: dict


dict01 = {'name': 'bavdu', 'age': 18, 'sex': 'man'}
dict02 = dict({'name': 'bavdu', 'age': 18, 'sex': 'man'})
dict03 = dict([('name', 'bavdu'), ('age', 18), ('sex', 'man')])
dict04 = dict(name='bavdu', age=18, sex='man')

dict05 = {
    'cpu': {
        'rate': {},
        'core': {},
        'GHZ': {}
    },
    'memory': {
        'rate': {},
        'size': {},
    }
}

print(dict05)
