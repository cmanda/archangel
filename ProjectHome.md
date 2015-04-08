Archangel is an advanced content filter with much of the same functionality of Dansguardian, but rewritten as an ICAP server in Python. The main reason I started this project is because I wanted a filter that had the same power as Dansguardian in regards to customizing block criteria but that also allowed filtering of traffic over HTTPS. I also wanted to make it more extendable by allowing users to create their own blocking modules.

Dansguardian currently is designed as a sort of front-end for a proxy server scanning outgoing requests as well as scanning cached pages (from the proxy). The way Archangel works is as an ICAP server; that is, it interfaces with a ICAP-capable proxy server (like Squid). In this setup, the proxy interfaces with Archangel to check HTTP requests and responses as they are received from the client and remote server.

It should be noted that Archangel, as it is, does not support anti-virus filtering. This feature may be implemented later, or you can just find another ICAP service that provides this functionality.

Archangel uses the PyICAP library to implement the ICAP functionality.