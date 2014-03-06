import xml.etree.ElementTree as ET
import collections

def CompareAttributes(e1, e2):
	#print('collections.Counter(e1)' + str(collections.Counter(e1)))
	#print('collections.Counter(e2)' + str(collections.Counter(e2)))
	return collections.Counter(e1.attrib) == collections.Counter(e2.attrib)

def CompareElement(e1, e2):
	if e1.tag == e2.tag and e1.text == e2.text:
		attributesMatch = CompareAttributes(e1, e2)
		#print('attributesMatch = ' + str(attributesMatch))
		if attributesMatch:
			children1 = sorted(list(e1), key = lambda x: x.tag)
			children2 = sorted(list(e2), key = lambda x: x.tag)
			childrenMatch = False
			if len(children1) == len(children2):
				childrenMatch = True
				for i in range(len(children1)):
					if not CompareElement(children1[i], children2[i]):
						print('children do not match - ' + str(children1[i]) + '----' + str(children2[i]))
						return False
			return childrenMatch
		
	#print('CompareElement (False) - ' + str(e1) + '----' + str(e2))
	return False

#tree1 = ET.parse('/Users/skhade/sushant/Sushant/C_drv/Desktop/temp/PurchaseResponse.xml')
#tree2 = ET.parse('/Users/skhade/sushant/Sushant/C_drv/Desktop/temp/PurchaseResponseCopy.xml')

option = 0
while option != 1 and option != 2:
	print 'Enter input format:'
	print '1.Filename'
	print '2.XmlString'
	option = int(raw_input())


if option == 1:
	print 'Enter filename'
	inputstring = raw_input()
	tree1 = ET.parse(inputstring)
elif option == 2:
	print 'Enter xmlstring'
	inputstring = raw_input()
	tree1 = ET.fromstring(inputstring)

option = 0
while option != 1 and option != 2:
	print 'Enter input format:'
	print '1.Filename'
	print '2.XmlString'
	option = int(raw_input())

if option == 1:
	print 'Enter filename'
	inputstring = raw_input()
	tree2 = ET.parse(inputstring)
elif option == 2:
	print 'Enter xmlstring'
	inputstring = raw_input()
	tree2 = ET.fromstring(inputstring)

print CompareElement(tree1.getroot(), tree2.getroot())
