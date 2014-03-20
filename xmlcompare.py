import xml.etree.ElementTree as ET
import collections
import itertools
import sys
from colorama import init, Fore

init()

def PrintElement(element, level):
	while level > 0:
		sys.stdout.write('\t')
		level -= 1

	print ET.tostring(element).strip()

def PrintAttributes(e1, e2):
	for key, value in e1.attrib:
		sys.stdout.write(' ' + key + '="' + value + '"')

def CompareAndPrintElement(e1, e2, level):
	if e1 == None:
		sys.stdout.write(Fore.GREEN)
		PrintElement(e2, level)
		sys.stdout.write(Fore.RESET)
		return

	if e2 == None:
		sys.stdout.write(Fore.RED)
		PrintElement(e1, level)
		sys.stdout.write(Fore.RESET)
		return

	if e1.tag == e2.tag:
		#if ET.tostring(e1).strip().endswith('/>'):
		#	templevel = level
		#	while templevel > 0:
		#		sys.stdout.write('\t')
		#		templevel -= 1

		#	print ET.tostring(e1).strip()

		elementName = splitHeadTail(ET.tostring(e1))
		templevel = level
		while templevel > 0:
			sys.stdout.write('\t')
			templevel -= 1

		if not CompareAttributes(e1, e2):
			sys.stdout.write(elementName.head[0:elementName.find(ET.tostring(e1).strip())+len(e1.tag)])
			PrintAttributes(e1, e2)
			if ET.tostring(e1).strip().endswith('/>'):
				sys.stdout.write('/>')
			else:
				sys.stdout.write('>')
		else:
			if ET.tostring(e1).strip().endswith('/>'):
				#templevel = level
				#while templevel > 0:
				#	sys.stdout.write('\t')
				#	templevel -= 1

				print ET.tostring(e1).strip()
			else:
				print elementName.head.strip()

		children1 = sorted(list(e1), key = lambda x: x.tag)
		children2 = sorted(list(e2), key = lambda x: x.tag)

		if len(children1) == 0 and len(children2) == 0:
			templevel = level
			while templevel >= 0:
				sys.stdout.write('\t')
				templevel -= 1

			if e1.text == e2.text:
				print e1.text.strip()
			else:
				#templevel = level
				#while templevel > 0:
				#	sys.stdout.write('\t')
				#	templevel -= 1
				print Fore.RED + e1.text + Fore.GREEN +	e2.text + Fore.RESET

		i = 0
		while i < len(children1):
			j = 0
			removei = False
			while j < len(children2):
				removej = False
				if CompareElement(children1[i], children2[j]):
					removei = True
					removej = True

				if removej:
					children2.pop(j)
					break
				else:
					j += 1

			if removei:
				PrintElement(children1[i], level+1)
				children1.pop(i)
			else:
				i += 1

		#if len(children2) > len(children1):
		#	children1, children2 = children2, children1

		for x, y in itertools.izip_longest(children1, children2):
			CompareAndPrintElement(x, y, level+1)

		templevel = level
		while templevel > 0:
			sys.stdout.write('\t')
			templevel -= 1

		print elementName.tail.strip()

#			for i in range(math.min(len(children1), len(children2))):
#				#if CompareElement(children1[i], children[2]):
#				PrintElement(children1[i], children2[i])
#
#			if len(children1) > len(children2):
#				for i in range(len(children1) - len(children2)):
#					PrintElement(children1[i+1+len(children2)]

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
						#print('children do not match - ' + str(children1[i]) + '----' + str(children2[i]))
						return False
			return childrenMatch
		
	#print('CompareElement (False) - ' + str(e1) + '----' + str(e2))
	return False

def splitHeadTail(element):
	Token = collections.namedtuple('Token', ['head', 'tail'])
	headcount = element.find('>')
	tailcount = element.rfind('<')

	if headcount > 0:
		head = element[0:headcount+1]
	else:
		print 'Head could not be split' + element
		exit()
	
	if tailcount > 0:
		tail = element[tailcount:]
	else:
		print 'Tail could not be split' + element
		exit()
	
	return Token(head, tail)

def printTree(root):
	if ET.tostring(root).strip().endswith('/>'):
		print ET.tostring(root)
		return

	elementName = splitHeadTail(ET.tostring(root))
	print elementName.head
	if len(list(root)) > 0:
		for element in list(root):
			printTree(element)

	else:
		print root.text

	print elementName.tail


#init()
#print(Fore.RED + 'some red text')

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

CompareAndPrintElement(tree1.getroot(), tree2.getroot(), 0)
#if CompareElement(tree1.getroot(), tree2.getroot()):
#	print 'The two files are identical'
#else:
#	print 'The two files are different'

