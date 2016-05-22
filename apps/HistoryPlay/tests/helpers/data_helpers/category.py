# -*- encoding: utf-8 -*-
from apps.HistoryPlay.management.commands_helpers.insert import InsertHelperMixin
from apps.HistoryPlay.models.Category import Category


class CategoryHelper(InsertHelperMixin):
    entity = Category

    def set_data(self):
        self.objects_to_insert = [
            {
                "name": "Areas arquelogicas",
            },
            {
                "name": "Monumentos",
            },
            {
                "name": "Museos",
            }
        ]
