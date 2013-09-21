# -*- coding: utf-8 -*-

import xlrd, json
from django.conf import settings
from apps.rp.models.Hs import Hs
from apps.rp.models.ProductCategory import ProductCategory


class XlsToJsonParser(object):
    ROOT_PATH = settings.ROOT_PATH
    entity = None
    entities_to_insert = []
    xls = None
    sheet = 'Sheet 1'
    json = None

    def xls_reader(self):
        """
        Read the file.xls and return the sheet
        """
        if self.xls is None:
            return False
            #TODO verify the xls in more detail

        self.xls_path = self.ROOT_PATH[:-5] + 'apps/common/db_data/' + self.xls + '.xls'
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
        json_path = self.ROOT_PATH[:-5] + 'apps/common/db_data/json/' + self.json + '.json'
        file = open(json_path,'w')
        file.write(json.dumps(initial, indent=2))
        file.close()

    def process_xls(self):
        return True


class HsCategoriesReader(XlsToJsonParser):

    entity = Hs
    xls = 'CATEGORIES_SUBCATEGORIES_HS'
    sheet = 'Hoja1'
    json = 'hs_categories'

    def process_xls(self):
        nrows = self.sheet.nrows - 1
        current_row = 2

        while(current_row < nrows):

            name = str(self.sheet.cell(current_row, 1))
            code = str(self.sheet.cell(current_row, 2))
            father = str(self.sheet.cell(current_row, 3))
            self.entities_to_insert.append([name, code, father])
            current_row += 1


class HsChapterReader(XlsToJsonParser):

    entity = Hs
    xls = 'hs_capitulos_'
    sheet = 'Hoja4'
    json = 'hs_chapters'

    def process_xls(self):
        nrows = self.sheet.nrows - 1
        current_row = 0

        while(current_row < nrows):

            name = str(self.sheet.cell(current_row, 1))
            code = str(self.sheet.cell(current_row, 2))
            self.entities_to_insert.append([name, code])
            current_row += 1


class CategoryReader(XlsToJsonParser):

    entity = ProductCategory
    xls = 'product_category'

    def split_cell(self, cell):
        cat = str(cell).split('(')[1]
        return cat.split(',')

    def check_service(self, cat):
        if cat.find("Services") > -1 or cat.find("Service") > -1:
            return False
        else:
            return True

    def calculate_level(self, cat):
        if cat == 'root':
            return 0
        else:
            return int(cat.strip("cat"))

    def process_xls(self):
        number_of_rows = self.sheet.nrows - 1
        self.current_row = 0
        self.process(number_of_rows, -1, 'root', '')

    def process(self, number_of_rows, parent, level, parent_name):
        _parent_name = ''
        while self.current_row < number_of_rows:
            cell = self.sheet.cell(self.current_row, 0)
            category = self.split_cell(cell)
            number = self.calculate_level(category[0])
            if number <= parent:
                return True
            elif category[0] != level:
                if self.block is False:
                    self.process(number_of_rows, number-1, category[0], _parent_name)
                else:
                    self.current_row +=1
            else:
                self.block = False
                if self.check_service(category[2]) is True:
                    _parent_name = category[2]
                    if level == 'root':
                        cat = [category[2].replace('"','')]
                    else:
                        cat = [category[2].replace('"',''), parent_name.replace('"','')]
                    self.entities_to_insert.append(cat)
                else:
                    self.block = True
                self.current_row += 1
