# Lession 4.6: What is Your Birthday

# This lesson will involve us validating a user's birthday. Input validation is crucial
# in order to make sure data entered from the user can be processed without errors.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4175328805/e-48754024/m-48714316


import webapp2

form = """
<form method="post">
    What is your birthday?
    <br>
    <input type="text" name="month">
    <input type="text" name="day">
    <input type="text" name="year">

    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

app = webapp2.WSGIApplication([("/", MainPage)], debug = True)
