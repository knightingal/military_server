from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler


def print_hello():
  print("Hello")


class MilitaryHTTPRequestHandler(SimpleHTTPRequestHandler):
  pass


def run(server_class=HTTPServer, handler_class=MilitaryHTTPRequestHandler):
  server_address=('', 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()


if __name__ == "__main__":
  print_hello()
  run()