Xml Compare
===========

- This python script uses the xml.etree library to compare two xml files/strings.
- This script differs from a file diff in that this script compares all children of two corresponding nodes.
- Thus, the two xml files could have the same children in different order and this script will consider them as same.
- Two elements are equal only if their namespaces are also equal.
- This script also matches attributes and their values.

Let me know if you have any suggestions.
