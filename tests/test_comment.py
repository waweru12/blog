import unittest
from app.models import Comments
from app import db

class TestComment(unittest.TestCase):

    def setUp(self): 
        self.new_comments = Comments(id=11, comment="BOOM", user_id=2, post_id=2 )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments, Comments))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comments.id, 11)
        self.assertEquals(self.new_comments.comment, "BOOM")
        self.assertEquals(self.new_comments.user_id, 2)        
        self.assertEquals(self.new_comments.post_id, 2)

    def test_save_comment(self):
        self.new_comments.save_comment() 
self.assertTrue(len(Comments.query.all()) > 0)