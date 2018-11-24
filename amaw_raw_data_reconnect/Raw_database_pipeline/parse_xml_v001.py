import os,re,sys,xml
import xml.dom.minidom

##<pathurl>
filenames = []

_xmlfile = r"C:\Users\DOC\Desktop\1.xml"

doc = xml.dom.minidom.parse(_xmlfile)

mov = doc.getElementsByTagName('pathurl')

expertise = doc.getElementsByTagName("file")
##    print "%d expertise:" % expertise.length


for skill in expertise:
##    print ski
    filenames.append(skill.getAttribute("<pathurl>"))
##    print skill.getAttribute("id")

print filenames
##for i in filenames:
##    splitlines = i.split('/n')
##    print type(splitlines)
##    print splitlines[:-2]







