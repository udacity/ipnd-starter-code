# Lession 4.7: Escaping Templates

# Escaping HTML characters is an important function to learn because this prevents
# unintended HTML code from rendering on the browser, stopping malicious users from
# abusing your site.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-668210172

import os
import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Handler(Handler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list_html", items = items)

app = webapp2.WSGIApplication([("/", MainPage)])
