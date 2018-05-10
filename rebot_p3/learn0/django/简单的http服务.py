from wsgiref.simple_server import make_server

def runServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['hello wsgi'.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, runServer)
    httpd.serve_forever()