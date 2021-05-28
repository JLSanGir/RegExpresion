# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"INFO: ([\w ]*)(\[\#\d+])"

test_str = ("May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)")

subst = "Error: \\1 numero \\2"

# You can manually specify the number of replacements by changing the 4th argument
#result = re.sub(regex, subst, test_str)
result = re.findall(regex, test_str)

if result:
    print (result[0])