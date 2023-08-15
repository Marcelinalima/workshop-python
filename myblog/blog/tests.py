from django.test import TestCase
from django.contrib.auth import get_user_model

from models import Entry
# Create your tests here.
class EntryViewTest(TestCase):

    def setUp(self):
          self.user = get_user_model().objects.create(username='some_user')
          self.entry = Entry.objects.create(title='1-title', body='1-body', author=self.user)

    def tes_basic_view(self):
        response = self.cliente.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        
class HomePageTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.cliente.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')

    def test_no_entries(self):
        response = self.client.get('/')
        self.assertContains(response, 'Nosso blog ainda nao tem postagem.')    



class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), 'entries')

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)