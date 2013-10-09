# -*- encoding: utf-8 -*-
from apps.HistoryPlay.management.commands_helpers.insert import InsertHelperMixin
from apps.HistoryPlay.models.Question import Question
from apps.HistoryPlay.models.Place import Place


class QuestionHelper(InsertHelperMixin):
    entity = Question

    def set_data(self):
        self.objects_to_insert = [
            {
                "place": Place.objects.get(step=1),
                "name":"Pregunta 1",
                "image": "thmbs.jpg"
            },
            {
                "place": Place.objects.get(step=1),
                "name":"Pregunta 2",
                "image": "thmbs.jpg"
            },
            {
                "place": Place.objects.get(step=2),
                "name":"Pregunta Dificil",
                "image": "thmbs.jpg"
            }
        ]