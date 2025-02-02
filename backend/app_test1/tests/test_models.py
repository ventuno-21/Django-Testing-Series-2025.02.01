from django.test import TestCase
from app_test1.models import Writer
from model_bakery import baker

"""
Baker will make us an instance of model, 
but if we want specific data for some fields, 
we can override these fields like 
'firstname' & 'lastname' as in function: test_model_str2
"""


class TestWriterModel(TestCase):

    # setUp method will be run before each methods
    def setUp(self):
        self.writer = baker.make(Writer, firstname="user1", lastname="user1last")

    def test_model_str(self):
        writer2 = Writer.objects.create(
            firstname="user1",
            lastname="user1last",
            email="user@user1.com",
            country="Italy",
        )
        self.assertEqual(str(writer2), "user1 - user1last")

    def test_model_str2(self):
        # print(self.writer.email)
        self.assertEqual(str(self.writer), "user1 - user1last")
