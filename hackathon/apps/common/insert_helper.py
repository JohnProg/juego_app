# -*- coding: utf-8 -*-

import xlrd, json
from django.conf import settings
from apps.HistoryPlay.models.Place import Place


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
        xls_book = xlrd.open_workbook(self.xls_path)
        xls_sheet = xls_book.sheet_by_name(self.sheet)
        return xls_sheet

    def parse_to_json(self):
        """
        Convert the xls file data to json file
        """
        self.sheet = self.xls_reader()

        # Need to be implemented in the class to inherits
        self.process_xls()

        initial = { 'values' : self.entities_to_insert }
        json_path = self.ROOT_PATH[:-5] + '/apps/common/db_data/json/' + self.json + '.json'
        file = open(json_path,'w')
        file.write(json.dumps(initial, indent=2))
        file.close()

    def process_xls(self):
        return True


class MuseumHelper(XlsToJsonParser):

    entity = Place
    xls = 'Museo'
    sheet = 'Museos Lima'

    def insert(self):
        xls = self.xls_reader()
