import tornado.ioloop
import tornado.web

PORT = 8888

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.remote_ip)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":

    if os.name == 'posix':
        import setproctitle
        setproctitle.setproctitle('echo-server')  # Set the process title to echo-server

    print("Starting IP echo server...")

    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
