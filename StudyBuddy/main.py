import os

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import mail


import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Data(ndb.Model):
    """Sub model for representing an author."""
    email = ndb.StringProperty(indexed=False)
    gender = ndb.StringProperty(indexed=True)
    location = ndb.StringProperty(indexed=True)
    study = ndb.StringProperty(indexed=True)
    level = ndb.StringProperty(indexed=False)
    subject = ndb.StringProperty(indexed=True)
    topic = ndb.StringProperty(indexed=True)
    date = ndb.StringProperty(indexed=True)
    time = ndb.StringProperty(indexed=False)


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'LOGOUT'
        else:
            self.redirect(users.create_login_url(self.request.uri))
            url = users.create_login_url(self.request.uri)
            url_linktext = 'LOGIN'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            }
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render(template_values))


class AboutPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'LOGOUT'
        else:
            self.redirect(users.create_login_url(self.request.uri))
            url = users.create_login_url(self.request.uri)
            url_linktext = 'LOGIN'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            }
        template = JINJA_ENVIRONMENT.get_template("about.html")
        self.response.write(template.render(template_values))


class SessionsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'LOGOUT'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'LOGIN'
            self.redirect(users.create_login_url(self.request.uri))

        show = Data.query().order(Data.date)
        display = show.fetch()

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            'display': display,
            }

        template = JINJA_ENVIRONMENT.get_template("sessions.html")
        self.response.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        info = Data()
        info.email = user.email()
        info.location = self.request.get('location')
        info.study = self.request.get('study')
        info.level = self.request.get('level')
        info.subject = self.request.get('subject')
        info.topic = self.request.get('topic')
        info.date = self.request.get('date')
        info.time = self.request.get('time')
        info.gender = self.request.get('gender')
        info.put()
        template_values = {
            'user': user,
            'info.email': info.email,
            'info.location': info.location,
            'info.study': info.study,
            'info.level': info.level,
            'info.subject': info.subject,
            'info.topic': info.topic,
            'info.date': info.date,
            'info.time': info.time,
            'info.gender': info.gender,
            }

        template = JINJA_ENVIRONMENT.get_template("sessions.html")
        self.response.write(template.render(template_values))

        self.redirect("/sessions")


class ResultsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'LOGOUT'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'LOGIN'
            self.redirect(users.create_login_url(self.request.uri))

        search_value = self.request.get("search_value")
        search_type = self.request.get("search_type")

        if search_type == "location":
            results = Data.query(Data.location == search_value).order(Data.date)
        elif search_type == "study":
            results = Data.query(Data.study == search_value).order(Data.date)
        elif search_type == "gender":
            results = Data.query(Data.gender == search_value).order(Data.date)
        elif search_type == "subject":
            results = Data.query(Data.subject == search_value).order(Data.date)
        elif search_type == "topic":s
            results = Data.query(Data.topic == search_value).order(Data.date)
        elif search_type == "date":
            results = Data.query(Data.date == search_value).order(Data.time)

        result = results.fetch()

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            'result': result,
            }

        template = JINJA_ENVIRONMENT.get_template("results.html")
        self.response.write(template.render(template_values))

    def post(self):
        search_value = self.request.get('search')
        search_type = self.request.get('search_type')

        template_values = {
            'search_value': search_value,
            'search_type': search_type,
            }
        template = JINJA_ENVIRONMENT.get_template("sessions.html")
        self.response.write(template.render(template_values))

        self.redirect("/search?search_value={0}".format(search_value))


class DataChanges(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        sessions_delete = self.request.get('delete', allow_multiple=True)
        if len(sessions_delete) > 0:
            for delete in sessions_delete:
                session = Data.get_by_id(long(delete))
                session.key.delete()

        sessions_attend = self.request.get('attend', allow_multiple=True)
        if len(sessions_attend) > 0:
            for attend in sessions_attend:
                session = Data.get_by_id(long(attend))
                message = mail.EmailMessage(subject="Your session on dhs-studybuddy.appspot.com has an attendee!")
                message.sender = user.email()
                message.to = session.email
                message.body = """Your session (""" + session.location + session.subject + session.topic + session.date + session.time + """) has an attendee! (""" + user.email() + """) """

                message.send()

        self.redirect('/sessions')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage),
    ('/sessions', SessionsPage),
    ('/search', ResultsPage),
    ('/apply', DataChanges),
], debug=True)
