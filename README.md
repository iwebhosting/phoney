Phoney
======

Phoney is a simple web based Caller ID manager for Asterisk.

You can use the [CURL function][cf] to integrate it for incoming calls.

[cf]: https://wiki.asterisk.org/wiki/display/AST/Asterisk+11+Function_CURL

Phoney has no access controls and should not be connected to untrusted networks.

The Quick Start
---------------

	# Install the dependencies
	$ pip install -r requirements.txt

	# Customise the config file (/etc/phoney.cfg)

	# Run the web server! (Ideally run under WSGI-compatible wrapper)
	$ bin/phoney runserver -t 0.0.0.0


An example line you could add to your `from-external` Asterisk config is:

    exten => _X.,1,Set(CALLERID(name)=${CURL("http://127.0.0.1:5000/numbers/c/${EXTEN}",from=${CALLERID(num)})})


License
-------

Copyright (c) 2016, Aaron Brady  
Copyright (c) 2016, Interactive Web Solutions Ltd	


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
