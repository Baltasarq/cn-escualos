#!/usr/bin/env python
# (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging
import datetime
import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.appinfo import AppInfo
from model.member import Member
from model.trial import Trial
from model.news import News
from model.photo import Photo
from model.document import Document


class AdminHandler(webapp2.RequestHandler):
    def get(self):
        # Get user
        usr = Member.current()

        if not usr:
            return Member.show_error_unrecognized_usr(self)

        # Render
        try:
            jinja = jinja2.get_jinja2(app=self.app)

            template_values = {
                "usr": usr,
                "info": AppInfo,
                "last_documents": Document.query().order(-Document.added).fetch(20),
                "last_photos": Photo.query().order(-Document.added).fetch(20),
            }

            self.response.write(jinja.render_template("admin_old.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))
        return

    def post(self):
        op_trial = self.request.get("edOpTrial")
        op_news = self.request.get("edOpNews")
        op_photo = self.request.get("edOpPhoto")
        op_doc = self.request.get("edOpDoc")

        if op_trial and op_trial != "nop":
            # Pick up trial info
            trial_name = self.request.get("edTrialName")
            trial_comments = self.request.get("edRemarks")
            txt_date = self.request.get("edDate", datetime.date.today().isoformat())
            trial_date = datetime.datetime.strptime(txt_date, "%Y-%m-%d")

            # Doit
            if op_trial == "add" or op_trial == "modify":
                # Retrieve
                trial_poster = self.request.get("edPoster")

                if op_trial == "add":
                    trial = Trial()
                else:
                    trial = Trial.query(Trial.date == trial_date).get()
                    if not trial:
                        self.redirect("/error?msg=trial was not found")
                        return

                if trial_name: trial.name = trial_name
                if trial_date: trial.date = trial_date
                if trial_comments: trial.comments = trial_comments
                if trial_poster: trial.poster = trial_poster
                trial.put()
                time.sleep(1)
            elif op_trial == "delete":
                member = Trial.query(Trial.date == trial_date).get()
                if member:
                    member.key.delete()
                    time.sleep(1)
                else:
                    self.redirect("/error?msg=trial was not found")
                    return
            else:
                self.redirect("/error?msg=operation on trials not supported")
                return

        elif op_news and op_news != "nop":
            # Retrieve
            news_title = self.request.get("edTitle")
            news_body = self.request.get("edBody")
            news_url = self.request.get("edUrl")
            news_photo = self.request.get("edPhotoForNews", "")
            news_doc = self.request.get("edDocForNews", "")

            if op_news == "add":
                news = News()

                if news_title: news.title = news_title
                if news_body: news.body = news_body
                if news_url: news.url = news_url
                if news_photo: news.photo = ndb.Key(urlsafe=news_photo)
                if news_doc: news.doc = ndb.Key(urlsafe=news_doc)
                news.put()
                time.sleep(1)
            elif op_news == "delete":
                news = News.query(News.title == news_title).get()
                if news:
                    news.key.delete()
                    time.sleep(1)
                else:
                    self.redirect("/error?msg=news was not found")
                    return
            else:
                self.redirect("/error?msg=operation on news not supported")
                return

        elif op_photo and op_photo != "nop":
            # Retrieve
            photo_title = self.request.get("edPhotoTitle")
            photo_tags = self.request.get("edPhotoTags")
            photo_image = self.request.get("edPhotoImage")

            if op_photo == "add":
                photo = Photo()

                if photo_title: photo.title = photo_title
                if photo_tags: photo.tags = photo_tags.split(',')
                if photo_image: photo.image = photo_image
                photo.put()
                time.sleep(1)
            elif op_photo == "delete":
                photo = Photo.query(Photo.title == photo_title).get()
                if photo:
                    photo.key.delete()
                    time.sleep(1)
                else:
                    self.redirect("/error?msg=photo was not found")
                    return
            else:
                self.redirect("/error?msg=operation on photo not supported")
                return
        elif op_doc and op_doc != "nop":
            # Retrieve
            doc_title = self.request.get("edDocTitle")
            doc_tags = self.request.get("edDocTags")
            doc_file = self.request.get("edDocFile")

            if op_doc == "add":
                document = Document()

                if doc_title: document.title = doc_title
                if doc_tags: document.tags = doc_tags.split(',')
                if doc_file: document.file = doc_file
                document.put()
                time.sleep(1)
            elif op_doc == "delete":
                document = Document.query(Document.title == doc_title).get()
                if document:
                    document.key.delete()
                    time.sleep(1)
                else:
                    self.redirect("/error?msg=document was not found")
                    return
            else:
                self.redirect("/error?msg=operation on document not supported")
                return

        self.redirect("/admin_old")
        return


app = webapp2.WSGIApplication([
    ("/admin_old", AdminHandler),
], debug=True)
