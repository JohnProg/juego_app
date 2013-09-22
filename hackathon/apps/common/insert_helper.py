# -*- coding: utf-8 -*-

import xlrd, json
from django.conf import settings
from decimal import Decimal
from apps.HistoryPlay.models.Place import Place
from apps.HistoryPlay.models.Question import Question
from apps.HistoryPlay.models.Category import Category
from apps.HistoryPlay.models.Answer import Answer


class XlsToJsonParser(object):
    ROOT_PATH = settings.ROOT_PATH
    entity = None
    entities_to_insert = []
    xls = None
    sheet = 'pagina1'
    json = None

    def xls_reader(self):
        """
        Read the file.xls and return the sheet
        """
        if self.xls is None:
            return False
            #TODO verify the xls in more detail
        self.xls_path = self.ROOT_PATH + '/apps/common/db_data/' + self.xls + '.xls'
        xls_book = xlrd.open_workbook(self.xls_path, encoding_override="cp1252")
        xls_sheet = xls_book.sheet_by_name(self.sheet)
        return xls_sheet

    def insert_information(self):
        self.sheet = self.xls_reader()
        self.process_xls()

    def parse_type(self, data):
        data = str(data)
        data = data.replace("text:u", "")
        data = data.replace("'", "")
        data = data.replace("number:", "")
        data = data.replace("\xf3", "o")
        data = data.replace("\xe9", "e")
        data = data.replace("\xed", "i")
        data = data.replace("\\xbf", "¿")
        data = data.replace("\\xf1", "ñ")
        data = data.replace("\xe1", "'a")
        return data

    def process_xls(self):
        return True


class MuseumHelper(XlsToJsonParser):
    entity = Place
    xls = 'Museo'
    sheet = 'Museos Lima'
    json = 'museo'

    def process_xls(self):
        nrows = self.sheet.nrows - 1
        current_row = 1

        while(current_row < nrows):
            place = Place()
            place.category = Category.objects.get(name='museos')
            place.area = self.parse_type(self.sheet.cell(current_row,0))
            place.description = self.parse_type(self.sheet.cell(current_row, 1))
            place.name = self.parse_type(self.sheet.cell(current_row, 2))
            place.address = self.parse_type(self.sheet.cell(current_row, 3))
            place.district = self.parse_type(self.sheet.cell(current_row, 4))
            place.phone = self.parse_type(self.sheet.cell(current_row, 5))
            place.web_page = self.parse_type(self.sheet.cell(current_row, 6))
            place.schedule = self.parse_type(self.sheet.cell(current_row, 7))
            place.cost = self.parse_type(self.sheet.cell(current_row,8))
            place.latitud = self.parse_type(self.sheet.cell(current_row, 9))
            place.longitud = self.parse_type(self.sheet.cell(current_row,10))
            place.step = int(float(self.parse_type(self.sheet.cell(current_row,12))))
            place.save()
            current_row += 1

    def insert(self):
        self.parse_to_json()


class QuestionHelper(XlsToJsonParser):
    entity = Place
    xls = 'BD'
    sheet = 'Hoja1'

    def process_xls(self):
        nrows = self.sheet.nrows - 1
        current_row = 1

        while(current_row < nrows):
            museun_name = self.parse_type(self.sheet.cell(current_row,3))
            museun = Place.objects.get(name=museun_name)
            question = Question()
            question.name = self.parse_type(self.sheet.cell(current_row,1))
            imagen = int(float(self.parse_type(self.sheet.cell(current_row,2))))
            if imagen == 1:
                question.image = ''
            question.type = int(float(self.parse_type(self.sheet.cell(current_row,4))))
            question.place = museun
            question.save()
            current_row += 1

    def insert(self):
        self.parse_to_json()


class AnswerHelper(XlsToJsonParser):
    entity = Place
    xls = 'BD2'
    sheet = 'Hoja1'

    def process_xls(self):
        nrows = self.sheet.nrows - 1
        current_row = 1

        while(current_row < nrows):
            try:
                question_name = self.parse_type(self.sheet.cell(current_row,0))
                question = Question.objects.get(name=question_name)
                answer = Answer()
                answer.question = question
                answer.name = self.parse_type(self.sheet.cell(current_row,1))
                answer.is_correct = int(float(self.parse_type(self.sheet.cell(current_row,2))))
                answer.image = self.parse_type(self.sheet.cell(current_row,3))
                answer.save()
            except:
                pass
            current_row += 1

    def insert(self):
        self.parse_to_json()
