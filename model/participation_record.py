#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
from google.appengine.ext import ndb

from model.member import Member
from model.competition import Competition


class MemberParticipation(ndb.Model):
    member = ndb.KeyProperty(kind=Member, required=True, indexed=True)
    stays_for_lunch = ndb.BooleanProperty(default=False)
    payment = ndb.BlobProperty()
    comments = ndb.StringProperty(default="")


class MemberTest(ndb.Model):
    uid = ndb.IntegerProperty(required=True, indexed=True)
    member = ndb.KeyProperty(kind=Member, required=True, indexed=True)
    test_uid = ndb.IntegerProperty(required=True, default=-1)
    milliseconds = ndb.IntegerProperty(required=True, indexed=True)


class ParticipationRecord(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    competition = ndb.KeyProperty(kind=Competition, required=True, indexed=True)
    participants = ndb.StructuredProperty(MemberParticipation, repeated=True)
    participants_per_test = ndb.StructuredProperty(MemberTest, repeated=True)

    def add_participant_per_test(self, participant_per_test):
        uid = int(time.time())

        participant_per_test.uid = uid
        self.participants_per_test.append(participant_per_test)

        return uid

    def get_participant_per_test_for_uid(self, member_test_uid):
        toret = None

        for participant_per_test in self.participants_per_test:
            if (participant_per_test.uid == member_test_uid):
                toret = participant_per_test
                break

        return toret
    
    def get_participant_per_test(self, member_key, test_uid):
        toret = None
        
        for participant_per_test in self.participants_per_test:
            if (participant_per_test.member == member_key
            and participant_per_test.test_uid == test_uid):
                toret = participant_per_test
                break
            
        return toret

    def get_participant_info(self, member_key):
        toret = None

        if member_key:
            for member_participation in self.participants:
                if member_participation.member == member_key:
                    toret = member_participation
                    break

        return toret

    def remove_member_test_for_uid(self, uid):
        test = None

        for participant_per_test in self.participants_per_test:
            if participant_per_test.uid == uid:
                test = participant_per_test
                break

        if test:
            self.participants_per_test.remove(test)

        return

    def remove_member(self, member_key):
        participants_per_test_to_remove = []

        # Collect removals
        for participant_per_test in self.participants_per_test:
            if participant_per_test.member == member_key:
                participants_per_test_to_remove.append(participant_per_test)

        # Remove them
        for participant_per_test_to_remove in participants_per_test_to_remove:
            self.participants_per_test.remove(participant_per_test_to_remove)

        # Remove the member
        participant = self.get_participant_info(member_key)
        self.participants.remove(participant)

        return

    @staticmethod
    def retrieve_participation_record(req):
        id = None
        try:
            id = req.request.GET["id"]
        except ValueError:
            return req.redirect("/error?msg=Missing participation record id.")

        try:
            participation_record = ndb.Key(urlsafe=id).get()
        except:
            return req.redirect("/error?msg=No participation record for id: " + str(id))

        return participation_record
