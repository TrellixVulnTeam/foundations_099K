from cgi import parse_qs, escape

def hello_world():
    print("<html><head><title></title></head><body><p>HelloWorld!</body></html>")



if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Serving at localhost:8080")
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()