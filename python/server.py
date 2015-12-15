import BaseHTTPServer
import json
import urlparse

class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):

    # Respond to a POST request
    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        json_data = json.loads(post_data)
        print json_data['key']
        self.send_response(200)

if __name__ == '__main__':
    BaseHTTPServer.HTTPServer(('localhost', 8000), MyServer).serve_forever()