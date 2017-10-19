from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print ("GET requests are not supported....")
        self.wfile.write("<html><body><h1>Test server running....</h1><h3>GET requests are not supported. Try POST.</h3></body></html>")

    def do_POST(self):
        self._set_headers()
        print ("POST request accepted....")
        print (self.rfile.read(int(self.headers.getheader('Content-Length'))))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Test POST-server running....'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
