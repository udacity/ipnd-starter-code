# Lession 4.7: Writing a Basic Form

# We'll start off writing a basic form in HTML using multiline strings to understand how
# we can process and substitute our variables into the HTML string we created.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/e-662529352/m-684819008

import os
import webapp2

form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
<button>Add</button>
</form>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.write(form_html)

app = webapp2.WSGIApplication([("/", MainPage)
                              ],
                              debug=True)
