from django.test import TestCase
from .models import Post

bam = 'just a text'

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text=bam)

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_objects_name = f'{post.text}'
        self.assertEqual(expected_objects_name, bam)







