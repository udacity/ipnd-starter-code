# Lession 4.5: Hello Webapp World
#
# This starter code will illustrate how we can create a webserver that writes out
# a "Hello World" to the browser usig the webapp2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4150259168/m-48722218

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write("Hello, webapp World!")

app = webapp2.WSGIApplication([("/", MainPage)],
                               debug = True)
