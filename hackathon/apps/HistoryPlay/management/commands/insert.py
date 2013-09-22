# from django.core.management.base import BaseCommand
# from optparse import make_option
# from apps.sp.tests.Helpers.data_helpers.criterion_category import CriterionCategoryHelper
# from apps.common.insert_helper import CriterionHelper, CriterionDetailHelper
# from apps.HistoryPlay.models.Category import Category
# from apps.HistoryPlay.models.Answer import Answer
# from apps.HistoryPlay.models.HistoryPlay import HistoryPlay
# from apps.HistoryPlay.models.Place import Place
# from apps.HistoryPlay.models.Question import Question
#
#
# class Command(BaseCommand):
#     data_delete = False
#
#     option_list = BaseCommand.option_list + (
#         make_option('--delete',
#             action='store_true',
#             dest='delete',
#             default=False,
#             help='Delete data'),
#         )
#
#     def handle(self, *args, **options):
#         entity = args[0]
#
#         if options['delete']:
#             self.data_delete = True
#
#         if entity == 'all':
#             self.insert_category()
#             # self.insert_arqueologia()
#             # self.insert_momnumentos()
#             # self.insert_museo()
#
#     def insert_category(self):
#         if self.data_delete:
#             C.objects.all().delete()
#             self.stdout.write('delete data: criterion category. \n')
#         else:
#
#
#     def insert_arqueologia(self):
#         if self.data_delete:
#             CriterionCategory.objects.all().delete()
#             self.stdout.write('delete data: criterion category. \n')
#         else:
#             if CriterionCategory.objects.all().count() == 0:
#                 criterion_category_helper = CriterionCategoryHelper()
#                 criterion_category_helper.set_data()
#                 criterion_category_helper.insert_data()
#                 self.stdout.write('Successfully inserted data: criterion category. \n')
#             else:
#                 self.stdout.write('can not insert the data: criterion category. \n')
#
