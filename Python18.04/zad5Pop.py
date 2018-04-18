#!/usr/bin/env python
#encoding: utf-8

from xml.dom import minidom

doc = minidom.parse("wschody.xml")

els = doc.getElementsByTagName("sun")
miej = doc.getElementsByTagName("name")[0]

for el in els:
    godzina = el.getAttribute("rise")
    print("Miejscowosc: %s, Godzina wschodu to: %s ", miej.firstChild.data, godzina)

