import http.server
import random
from time import time
from prometheus_client import Histogram, start_http_server, Counter, Gauge, Summary

REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_worlds_exceptions_total',
                     'Exceptions serving Hello World.')
INPROGRESS = Gauge('hello_worlds_inprogress',
                   'Number of Heelo Worlds in progress')
LAST = Gauge('hello_worlds_last_time_seconds',
             'The last time a Hello World was served.')
LATENCY = Summary('hello_world_latency_seconds',
                  'Time for a request Hello World.')


class MyHandler(http.server.BaseHTTPRequestHandler):
    @EXCEPTIONS.count_exceptions()
    # @INPROGRESS.track_inprogress()
    # @LATENCY.time()
    def do_GET(self):
        REQUESTS.inc()
        INPROGRESS.inc()
        start = time.time()

        if random.random() < 0.2:
            LAST.set_to_current_time()
            INPROGRESS.dec()
            raise Exception

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

        LATENCY.observe(time.time() - start)
        LAST.set_to_current_time()
        INPROGRESS.dec()


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
