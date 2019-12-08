import xml.dom.minidom
import xml.etree.cElementTree as ET
doc=xml.dom.minidom.parse("Newxml.xml")
print (doc.nodeName)
elements=doc.getElementsByTagName("item")
for element in elements:
    print (element.attributes['name'].value)
    print (element.firstChild.data)
k=int(raw_input("Numebr of attribute to change"))
input=raw_input("New value")
elements[k-1].firstChild.nodeValue=input
for element in elements:
    print (element.attributes['name'].value)
    print (element.firstChild.data)
with open('newitems.xml', 'w') as f:
        f.write(doc.toxml())











