# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")

# Instructor Notes:
# Suggest to print out template_dir to see how the file path is being constructured.
# You can find the print out in the Logs in Google App Engine (GAE). For Windows and Mac users,
# you need to click on the "Logs" button to be able to see the print messages

# print "###" # These hash marks helps us locate our print statement from the rest of the messages
              # Google App Engine gives us
# print template_dir
# print "###"

# For Windows Users, you need to add in a logging flag for GAE to print out your
# statements appropriately. Please go here to download the "Google App Engine Troubleshooting"
# guide to learn how to add in the logging flag:
# https://www.udacity.com/course/viewer#!/c-nd000/l-4166899177/m-3974308850

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        output = form_html
        output_hidden = ""

        items = self.request.get_all("food")
        if items:
            output_items = ""
            for item in items:
                output_hidden += hidden_html % item
                output_items += item_html % item

            output_shopping = shopping_list_html % output_items
            output += output_shopping

        output = output % output_hidden

        self.write(output)

app = webapp2.WSGIApplication([("/", MainPage)])
