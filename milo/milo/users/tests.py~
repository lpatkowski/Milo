# coding: utf-8
from django.test import TestCase
from milo.users.models import User
from milo.users.templatetags.user_tags import *
import sys
from datetime import date

class UserTest(TestCase):
    
    def setUp(self):
        self.user = User(first_name=u"Łukasz",
                         last_name=u"Patkowski",
                         username="lpatkowski",
                         email="lpatkowski@gmail.com",
                         birthday_date=date(1986,11,18))
        self.user.save()

        print "User %s" % self.user
                     
        
    def test_getUser(self):
        self.assertIsNotNone(self.user, "User cannot be None")
        self.assertEquals(self.user.email, 'lpatkowski@gmail.com', "Invalid Useremail")
        print >> sys.stdout,  "User %s" % self.user

    def test_random_number_ranges(self): 
        self.assertTrue(self.user.random_number >= 1 and self.user.random_number <=100, "Invalid user random number")
        print >> sys.stdout,  "Random number: %d OK" % self.user.random_number

    def test_allowed_templatetag(self):
        self.assertEquals(user_allowed(self.user), "allowed", "Allowed templatetag FAILED")
        print >> sys.stdout,  "Allowed templatetag OK"

        
    def test_bizzfuzz_templatetag(self):
        self.user.random_number = 3
        self.assertEquals(modulo(self.user.random_number), "Bizz", "Modulo templatetag Bizz FAILED")
        print >> sys.stdout,  "Modulo Bizz templatetag OK"

        self.user.random_number = 5
        self.assertEquals(modulo(self.user.random_number), "Fuzz", "Modulo templatetag Fuzz FAILED")
        print >> sys.stdout,  "Modulo Fuzz templatetag OK"

        self.user.random_number = 15
        self.assertEquals(modulo(self.user.random_number), "BizzFuzz", "Modulo templatetag BizzFuzz FAILED") 
        print >> sys.stdout,  "Modulo BizzFuzz templatetag OK"
