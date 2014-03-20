Xml Compare
===========

- This python script uses the xml.etree library to compare two xml files/strings.
- This script differs from a file diff in that this script compares all children of two corresponding nodes.
- Thus, the two xml files could have the same children in different order and this script will consider them as same.
- Two elements are equal only if their namespaces are also equal.
- This script also matches attributes and their values.
- This script uses colorama (https://pypi.python.org/pypi/colorama) to highlight the differences.
- The output shows changes to be made to the first xml to make it equal to the second xml. For example, content which is only present in the first xml is marked in red as it has to be deleted to match the second xml. Content which is present only in the second xml is marked in green as it needs to be added to the first xml. Content which has to be replaced, the old content in first xml is marked in red and the content in the second xml is marked in green. Content which matches both files is in white.

Let me know if you have any suggestions.
