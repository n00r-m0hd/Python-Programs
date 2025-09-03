# In this program we will learn about RegEx, Regualar Expression

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re

txt = "If you want to be a programmer so you will must be curious and explorer."

# x = re.search("^If explore$",txt)
# x = re.findall("you",txt)
x = re.search("you",txt)

print(x)