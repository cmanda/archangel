# Module for blocking banned url regexes

import re

from utils.load_config_file import loadFile
from utils.blockpage import BlockPage
from utils.matchresult import MatchResult

ROOT_PREFIX = ''
config_file = ''
regex_list = None

# API definitions starts here

category = "Banned regex url"
handler = None

def init(parser, handler):
    ROOT_PREFIX = parser.get('app_config', 'programroot')
    config_file = ROOT_PREFIX + "/lists/bannedregexpurllist"
    regex_list = loadFile(config_file)
    handler = handler

# Scan algorithm
def scan(request):
    result = MatchResult()
    url = request.enc_req[1]
    for regex in regex_list:
        match = re.search(regex, url)
        if match != None:
            result.matched = True
            result.category = category
            result.criteria = regex
            return result
    # No match
    return result

# Stop as soon as a match is found
stop_after_match = True

