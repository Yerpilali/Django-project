from django.test import TestCase
from store.models import Publisher, Developer

# Create your tests here.


class PublisherTestCase(TestCase):

    def setUp(self):
        Developer.objects.create(name_developer="Konami")
        Developer.objects.create(name_developer="scr")
        Publisher.objects.create(name_publisher='2K', developer_id_id=1)
        Publisher.objects.create(name_publisher='Konami', developer_id_id=2)
        Publisher.objects.create(name_publisher='Microsoft', developer_id_id=1)

    def test_publisher(self):
        name_publisher = Publisher.objects.get(name_publisher='Konami', )
        self.assertEqual(name_publisher.developer_id_id, 2)

    def test_publisher_1(self):
        name_publisher = Publisher.objects.get(name_publisher='Konami', )
        self.assertEqual(name_publisher.developer_id_id, 1)
