import SimpleHTTPServer
import SocketServer
import sys

PORT = sys.argv[1]
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", int(PORT)), Handler)
print "serving at port", PORT
httpd.serve_forever()