#!/usr/bin/env python

import requests
from MGModule import MGModule
import re
import sys

#search_term = "Make Noise Morphagene"
search_term = sys.argv[1]

print("Searching for: %s" % search_term)
url_main = "https://modulargrid.net"
module_slug = re.sub(" ", "-", search_term)
url = "%s/e/%s" % (url_main, module_slug)
response = requests.get(url)
num_alternates = 0

themodule = MGModule()

if response.status_code != 200:
    themodule.search(search_term, num_alternates)
else:
    themodule.initFromPage(response)
    themodule.render()
