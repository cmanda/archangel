The http matching module is used to match an HTTP request or response against a given criteria. For example, the banned regex url module is used to detect a given regex in the URL of the HTTP request. Each matching module is written in python and should follow a specific API. To enable a module, you have to place it in the _$PROGRAM\_ROOT/matching\_modules_ directory and add it to the _http\_req\_scanner_ or the _http\_res\_scanner_ section of the archangel.conf file. The syntax should be:

_module\_name=class\_name_

where module\_name represents the name of the module, specified by the filename (i.e. I call the banned regex url module banned\_regex\_url since its filename is banned\_regex\_url.py) and the class\_name is the name of the class (i.e. banned\_regex\_url class name is BannedRegexUrl).

# API #

constructor: receives as arguments the configuration parser passed from the main program. You will be using this to load any configuration data that you may have specified in the archangel.conf file that is needed by the scanner.

scan: this is the method used to scan the request or response. It takes the actual request or response as an argument and returns any data that will be used by the handler that is assigned to this module. For example, if the module uses the _blockpage_ handler, then the _scan_ method will return a _MatchResult_ object containing information on whether there was a match, what module detected the match, and what the match criteria was.

_handler_: this is just a string member of the class indicating the name of the module containing the handler for this class. For example, if your module blocks the page, then this string should be set to "blockpage".

_stop\_after\_scan_: this is a boolean member of the class that indicates whether scanning should stop after a match is found. If you are using the handler to block or allow the page after a match, for example, then this should be set to true, since those handlers send an ICAP response to the proxy server. However, if you use another handler that merely modifies the data, then you might want to set this to false, as other modifications may need to take place before sending the data and returning.