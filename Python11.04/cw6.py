#!/usr/bin/env python
#encoding: utf-8

from xml.dom import minidom

doc = minidom.parse('test.xml')

els = doc.getElementsByTagName('el')

for el in els:
    sid = el.getAttribute('id')
    test = el.getElementsByTagName('test')[0]
    print ('id: %s, val: %s' %(sid,test.firstChild.data))
