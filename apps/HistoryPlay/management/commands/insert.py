from django.core.management.base import BaseCommand
from optparse import make_option
from apps.common.insert_helper import MuseumHelper
from apps.HistoryPlay.models.Category import Category
from apps.HistoryPlay.models.Answer import Answer
from apps.HistoryPlay.models.HistoryPlay import HistoryPlay
from apps.common.insert_helper import QuestionHelper
from apps.common.insert_helper import AnswerHelper
from apps.HistoryPlay.models.Place import Place
from apps.HistoryPlay.models.Question import Question


class Command(BaseCommand):
    data_delete = False

    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete data'),
        )

    def handle(self, *args, **options):
        entity = args[0]

        if options['delete']:
            self.data_delete = True

        if entity == 'all':
            self.insert_category()
            self.insert_museos()
            self.insert_question()
            self.insert_answer()

        if entity == 'category':
            self.insert_category()

        if entity == 'museo':
            self.insert_museos()

        if entity == 'question':
            self.insert_question()

        if entity == 'answer':
            self.insert_answer()

    def insert_category(self):
        if self.data_delete:
            Category.objects.all().delete()
            self.stdout.write('delete data: Category. \n')
        else:
            names = ['museos', 'monumentos', 'Sitios Arqueologicos']
            for name in names:
                category = Category()
                category.name = name
                category.save()

    def insert_museos(self):
        category_museo = Category.objects.get(name='museos')
        category_monumento = Category.objects.get(name='monumentos')
        category_arqueologo = Category.objects.get(name='Sitios Arqueologicos')
        if self.data_delete:
            Place.objects.filter(category=category_museo).delete()
            self.stdout.write('delete data: museo. \n')
        else:
            if Place.objects.filter(category=category_museo).count() == 0:
                criterion_category_helper = MuseumHelper()
                criterion_category_helper.insert_information()
                self.stdout.write('Successfully inserted data: museo. \n')
            else:
                self.stdout.write('can not insert the data: museo \n')

    def insert_question(self):
        if self.data_delete:
            Question.objects.all().delete()
            self.stdout.write('delete data: question. \n')
        else:
            if Question.objects.filter().count() == 0:
                question_helper = QuestionHelper()
                question_helper.insert_information()
                self.stdout.write('Successfully inserted data: question. \n')
            else:
                self.stdout.write('can not insert the data: question \n')

    def insert_answer(self):
        if self.data_delete:
            Answer.objects.all().delete()
            self.stdout.write('delete data: answer. \n')
        else:
            if Answer.objects.filter().count() == 0:
                answer_helper = AnswerHelper()
                answer_helper.insert_information()
                self.stdout.write('Successfully inserted data: answer. \n')
            else:
                self.stdout.write('can not insert the data: answer \n')
