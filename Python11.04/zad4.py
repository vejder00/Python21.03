#!/usr/bin/env python
#encoding: utf-8

from xml.dom import minidom

doc = minidom.parse("wschody.xml")

miejscowosc = doc.getElementsByTagName('name')[0]
wschod = doc.getElementsByTagName('sun rise')

print(wschod)

