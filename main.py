import datetime
from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

from paddleocr import PaddleOCR, draw_ocr

def print_hello():
  print("Hello")


class MilitaryHTTPRequestHandler(SimpleHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header("content-length", str(len("MilitaryHTTPRequestHandler")))
    self.end_headers()

    self.wfile.write(bytes("MilitaryHTTPRequestHandler", "UTF-8"))

  def do_POST(self):
    content_length = int(self.headers.get("content-length"))
    body = self.rfile.read(content_length)

    time = datetime.datetime.now()
    now = time.strftime("%d-%m-%Y-%H:%M:%S")

    pic_file = open(now + ".jpg", "wb+")
    pic_file.write(body)
    pic_file.close()

    img = Image.open(now + ".jpg").convert("RGB")
    img.save(now + "jp.jpg")


    ocr = PaddleOCR(use_angle_cls=True, lang='ch')

    result = ocr.ocr(body, cls=True)
    if result is not None:
      for idx in range(len(result)):
          res = result[idx]
          if res is not None:
            for line in res:
                print(line)

    self.send_response(200)
    self.send_header("content-length", "0")
    self.end_headers()


def run(server_class=HTTPServer, handler_class=MilitaryHTTPRequestHandler):
  server_address=('', 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()


if __name__ == "__main__":
  print_hello()
  run()