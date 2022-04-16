#!/usr/bin/python3
source = open('/tmp/passwd', 'rb').read()
dest = open('/tmp/passwd2', 'wb')
for i in source:
	dest.write(bytes([i ^ 0x9b]))
