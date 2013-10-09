# -*- encoding: utf-8 -*-
from apps.HistoryPlay.management.commands_helpers.insert import InsertHelperMixin
from apps.HistoryPlay.models.Place import Place
from apps.HistoryPlay.models.Category import Category


class PlaceHelper(InsertHelperMixin):
    entity = Place

    def set_data(self):
        self.objects_to_insert = [
            {
                "area": "Area del museo",
                "name": "Museo inolvidable",
                "category":Category.objects.latest('created'),
                "description":"MUseo divertido",
                "address":"Av. Arequipa 354",
                "district":"Lince",
                "phone":"123456",
                "web_page": "LAINOLVIDALE.COM",
                "schedule": "2:00 - 3:00",
                "cost": "300",
                "latitud":"123123213.-213213",
                "longitud": "47656832113.3223",
                "step":1
            },
            {
                "area": "Museo",
                "name": "Museo de la Nacion",
                "category":Category.objects.latest('created'),
                "description":"Museo de presentaciones de heroes historicos",
                "address":"Av. Colon 354",
                "district":"Cercado de LIma",
                "phone":"4321321",
                "web_page": "Museodelaacion.COM",
                "schedule": "2:00 - 3:00",
                "cost": "30",
                "latitud":"123123213.-213213",
                "longitud": "47656832113.3223",
                "step":2
            }
        ]
