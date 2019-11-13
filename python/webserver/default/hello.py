#!/usr/bin/env python

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = '''<html>
    <head>
        <title>HELLO-WORLD SERVER</title>
    </head>
    <body>
        <h1>Hello</h1>
        <p>world!</p>
    </body>
    </html>
'''
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8000)
print('Serving at http://0.0.0.0:{}'.format(server_address[1]))
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
