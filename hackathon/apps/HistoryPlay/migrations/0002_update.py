# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'HistoryPlay_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('HistoryPlay', ['Profile'])

        # Adding model 'Question'
        db.create_table(u'HistoryPlay_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Question'])

        # Adding model 'HistoryPlay'
        db.create_table(u'HistoryPlay_historyplay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history_play_set', to=orm['HistoryPlay.Place'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history_play_set', to=orm['HistoryPlay.Profile'])),
            ('progress', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['HistoryPlay'])

        # Adding model 'Answer'
        db.create_table(u'HistoryPlay_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer_set', to=orm['HistoryPlay.Answer'])),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Answer'])

        # Adding model 'Place'
        db.create_table(u'HistoryPlay_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='place_set', to=orm['HistoryPlay.Category'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('web_page', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('schedule', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('latitud', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('longitud', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Place'])

        # Adding model 'Category'
        db.create_table(u'HistoryPlay_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'HistoryPlay_profile')

        # Deleting model 'Question'
        db.delete_table(u'HistoryPlay_question')

        # Deleting model 'HistoryPlay'
        db.delete_table(u'HistoryPlay_historyplay')

        # Deleting model 'Answer'
        db.delete_table(u'HistoryPlay_answer')

        # Deleting model 'Place'
        db.delete_table(u'HistoryPlay_place')

        # Deleting model 'Category'
        db.delete_table(u'HistoryPlay_category')


    models = {
        'HistoryPlay.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer_set'", 'to': "orm['HistoryPlay.Answer']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.historyplay': {
            'Meta': {'object_name': 'HistoryPlay'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history_play_set'", 'to': "orm['HistoryPlay.Place']"}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history_play_set'", 'to': "orm['HistoryPlay.Profile']"}),
            'progress': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'HistoryPlay.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'place_set'", 'to': "orm['HistoryPlay.Category']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'web_page': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.question': {
            'Meta': {'object_name': 'Question'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['HistoryPlay']