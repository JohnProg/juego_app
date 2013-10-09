import json
from django.test.testcases import TestCase
from django.test.client import RequestFactory
from django.test.client import Client
from django.contrib.auth.models import User
from apps.HistoryPlay.models.Category import Category
from apps.HistoryPlay.models.Question import Question
from apps.HistoryPlay.models.Place import Place
from apps.HistoryPlay.views.player.game import QuestionView, QuestionJsonView
from apps.HistoryPlay.tests.helpers.data_helpers.category import CategoryHelper
from apps.HistoryPlay.tests.helpers.data_helpers.question import QuestionHelper
from apps.HistoryPlay.tests.helpers.data_helpers.place import PlaceHelper


class QuestionViewTest(TestCase):
 
    def setUp(self):
        self.request_factory = RequestFactory()
        self.client = Client()
        self.category_helper = CategoryHelper()
        self.place_helper = PlaceHelper()
        self.question_helper = QuestionHelper()
        self.user = User.objects.create(username='user')

    def _insert_data(self):
        self.category_helper.set_data()
        self.category_helper.insert_data()

        self.place_helper.set_data()
        self.place_helper.insert_data()

        self.question_helper.set_data()
        self.question_helper.insert_data()

    def test_insert_data(self):
        self._insert_data()
        self.assertTrue(Category.objects.all().count > 0)
        self.assertTrue(Place.objects.all().count > 0)
        self.assertTrue(Question.objects.all().count>0)

    def test_question_View(self):
        self._insert_data()
        place = Place.objects.get(step=1)
        view = QuestionView.as_view()
        request = self.request_factory.get(
            'question', kwargs={'place':place.id}
        )
        request.user = self.user
        response = view(request, place=place.id)
        self.assertEqual(response.status_code, 200)

    def test_question_json(self):
        self._insert_data()
        place = Place.objects.get(step=1)
        view = QuestionJsonView.as_view()
        request = self.request_factory.get(
            'json-question-place', kwargs={'place':place.id}
        )
        request.user = self.user
        response = view(request, place=place.id)
        self.assertEqual(response.status_code, 200)
        data_response = json.loads(response.content)
        self.assertEqual(len(data_response.get('question')), 2)